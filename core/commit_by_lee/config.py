"""Configuration management"""

import os
import yaml
from pathlib import Path
from typing import Optional
import logging

from .models.schemas import ConfigModel, Language, CommitStyle

logger = logging.getLogger(__name__)


class Config:
    """
    Configuration manager for Commit by Lee
    """

    DEFAULT_CONFIG_PATH = Path.home() / ".commit-by-lee.yaml"
    PROJECT_CONFIG_NAME = ".commit-by-lee.yaml"

    def __init__(self, config_path: Optional[Path] = None):
        """
        Initialize configuration

        Args:
            config_path: Path to config file (optional)
        """
        self.config_path = config_path or self.DEFAULT_CONFIG_PATH
        self.config: ConfigModel = self._load_config()

    def _load_config(self) -> ConfigModel:
        """
        Load configuration from file and environment variables

        Returns:
            ConfigModel object
        """
        # Start with defaults
        config_dict = {}

        # Load from file if exists
        if self.config_path.exists():
            try:
                with open(self.config_path, 'r') as f:
                    file_config = yaml.safe_load(f)
                    if file_config:
                        config_dict.update(file_config)
                logger.info(f"Loaded config from {self.config_path}")
            except Exception as e:
                logger.warning(f"Failed to load config file: {e}")

        # Override with environment variables
        env_overrides = {
            'ollama_host': os.getenv('OLLAMA_HOST'),
            'ollama_model': os.getenv('OLLAMA_MODEL'),
            'ollama_timeout': self._parse_int(os.getenv('OLLAMA_TIMEOUT')),
            'ollama_temperature': self._parse_float(os.getenv('OLLAMA_TEMPERATURE')),
            'ollama_max_tokens': self._parse_int(os.getenv('OLLAMA_MAX_TOKENS')),
            'language': os.getenv('COMMIT_BY_LEE_LANGUAGE'),
            'style': os.getenv('COMMIT_BY_LEE_STYLE'),
            'auto_commit': self._parse_bool(os.getenv('COMMIT_BY_LEE_AUTO_COMMIT')),
        }

        # Apply non-None environment overrides
        for key, value in env_overrides.items():
            if value is not None:
                config_dict[key] = value

        return ConfigModel(**config_dict)

    def save(self, path: Optional[Path] = None):
        """
        Save current configuration to file

        Args:
            path: Path to save config (default: use config_path)
        """
        save_path = path or self.config_path

        try:
            with open(save_path, 'w') as f:
                yaml.dump(self.config.model_dump(), f, default_flow_style=False)
            logger.info(f"Saved config to {save_path}")
        except Exception as e:
            logger.error(f"Failed to save config: {e}")
            raise

    @staticmethod
    def _parse_int(value: Optional[str]) -> Optional[int]:
        """Parse integer from string"""
        if value is None:
            return None
        try:
            return int(value)
        except ValueError:
            return None

    @staticmethod
    def _parse_float(value: Optional[str]) -> Optional[float]:
        """Parse float from string"""
        if value is None:
            return None
        try:
            return float(value)
        except ValueError:
            return None

    @staticmethod
    def _parse_bool(value: Optional[str]) -> Optional[bool]:
        """Parse boolean from string"""
        if value is None:
            return None
        return value.lower() in ('true', '1', 'yes', 'on')

    @classmethod
    def load_project_config(cls, project_path: Path) -> Optional['Config']:
        """
        Load project-specific configuration

        Args:
            project_path: Path to project directory

        Returns:
            Config object or None if no project config found
        """
        config_path = project_path / cls.PROJECT_CONFIG_NAME

        if config_path.exists():
            return cls(config_path)

        return None

    def get(self, key: str, default=None):
        """
        Get configuration value

        Args:
            key: Configuration key
            default: Default value if key not found

        Returns:
            Configuration value
        """
        return getattr(self.config, key, default)

    def update(self, **kwargs):
        """
        Update configuration values

        Args:
            **kwargs: Key-value pairs to update
        """
        for key, value in kwargs.items():
            if hasattr(self.config, key):
                setattr(self.config, key, value)
                logger.info(f"Updated config: {key} = {value}")
