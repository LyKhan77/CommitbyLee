"""
Commit by Lee - AI-powered Git Commit Message Generator

Generate commit messages automatically using Qwen3:4B via Ollama.
"""

__version__ = "0.1.0"
__author__ = "Lee"
__description__ = "Generate commit messages otomatis dengan AI, 100% lokal & privasi terjaga"

from .ollama_client import OllamaClient
from .diff_analyzer import DiffAnalyzer
from .llm_generator import CommitMessageGenerator
from .config import Config

__all__ = [
    "OllamaClient",
    "DiffAnalyzer",
    "CommitMessageGenerator",
    "Config",
]
