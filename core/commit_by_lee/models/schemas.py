"""Pydantic models for data validation"""

from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum


class CommitType(str, Enum):
    """Conventional commit types"""
    FEAT = "feat"
    FIX = "fix"
    DOCS = "docs"
    STYLE = "style"
    REFACTOR = "refactor"
    TEST = "test"
    CHORE = "chore"
    PERF = "perf"
    CI = "ci"
    BUILD = "build"


class Language(str, Enum):
    """Supported languages"""
    INDONESIAN = "id"
    ENGLISH = "en"


class CommitStyle(str, Enum):
    """Commit message styles"""
    CONVENTIONAL = "conventional"
    EMOJI = "emoji"
    SIMPLE = "simple"


class CommitMessage(BaseModel):
    """Commit message model"""
    type: CommitType
    scope: Optional[str] = None
    subject: str
    body: Optional[str] = None
    footer: Optional[str] = None
    breaking_change: bool = False

    def format_conventional(self) -> str:
        """Format as conventional commit"""
        message = f"{self.type.value}"
        if self.scope:
            message += f"({self.scope})"
        message += f": {self.subject}"

        if self.body:
            message += f"\n\n{self.body}"
        if self.footer:
            message += f"\n\n{self.footer}"
        if self.breaking_change:
            message += f"\n\nBREAKING CHANGE: {self.subject}"

        return message

    def format_emoji(self) -> str:
        """Format with emoji"""
        emoji_map = {
            CommitType.FEAT: "✨",
            CommitType.FIX: "🐛",
            CommitType.DOCS: "📝",
            CommitType.STYLE: "💄",
            CommitType.REFACTOR: "♻️",
            CommitType.TEST: "✅",
            CommitType.CHORE: "🔧",
            CommitType.PERF: "⚡",
            CommitType.CI: "👷",
            CommitType.BUILD: "📦",
        }

        emoji = emoji_map.get(self.type, "")
        message = f"{emoji} {self.type.value}"
        if self.scope:
            message += f"({self.scope})"
        message += f": {self.subject}"

        if self.body:
            message += f"\n\n{self.body}"

        return message

    def format_simple(self) -> str:
        """Format as simple message"""
        return self.subject


class DiffStats(BaseModel):
    """Diff statistics"""
    files_changed: int = 0
    insertions: int = 0
    deletions: int = 0
    files: List[str] = Field(default_factory=list)


class DiffAnalysis(BaseModel):
    """Git diff analysis result"""
    raw_diff: str
    stats: DiffStats
    file_types: List[str] = Field(default_factory=list)
    suggested_scope: Optional[str] = None
    suggested_type: Optional[CommitType] = None


class ConfigModel(BaseModel):
    """Configuration model"""
    # Ollama settings
    ollama_host: str = "https://ollama.iotech.my.id"
    ollama_model: str = "qwen3:4b"
    ollama_timeout: int = 30
    ollama_temperature: float = 0.7
    ollama_max_tokens: int = 200

    # App settings
    language: Language = Language.INDONESIAN
    style: CommitStyle = CommitStyle.CONVENTIONAL
    auto_commit: bool = False

    # Git settings
    scope_mappings: dict = Field(default_factory=lambda: {
        "src/auth/": "auth",
        "src/ui/": "ui",
        "src/api/": "api",
        "src/utils/": "utils",
        "src/core/": "core",
    })
    allowed_commit_types: List[CommitType] = Field(default_factory=lambda: [
        CommitType.FEAT,
        CommitType.FIX,
        CommitType.DOCS,
        CommitType.REFACTOR,
        CommitType.TEST,
        CommitType.CHORE,
    ])
