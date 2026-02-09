"""Git diff analyzer"""

import subprocess
import re
from typing import List, Optional
from pathlib import Path
import logging

from .models.schemas import DiffAnalysis, DiffStats, CommitType

logger = logging.getLogger(__name__)


class DiffAnalyzer:
    """
    Analyze git diff to extract meaningful information
    """

    def __init__(self, repo_path: Optional[str] = None):
        """
        Initialize diff analyzer

        Args:
            repo_path: Path to git repository (default: current directory)
        """
        self.repo_path = Path(repo_path) if repo_path else Path.cwd()

    def get_staged_diff(self) -> str:
        """
        Get git diff for staged changes

        Returns:
            Raw diff string

        Raises:
            subprocess.CalledProcessError: If git command fails
        """
        try:
            result = subprocess.run(
                ["git", "diff", "--staged"],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to get git diff: {e}")
            raise
        except FileNotFoundError:
            logger.error("Git not found. Please ensure git is installed.")
            raise

    def analyze_diff(self, diff: str) -> DiffAnalysis:
        """
        Analyze git diff and extract statistics

        Args:
            diff: Raw git diff string

        Returns:
            DiffAnalysis object with statistics and suggestions
        """
        if not diff:
            logger.warning("Empty diff provided")
            return DiffAnalysis(raw_diff="", stats=DiffStats())

        stats = self._calculate_stats(diff)
        file_types = self._extract_file_types(diff)
        suggested_scope = self._suggest_scope(diff)
        suggested_type = self._suggest_type(diff, stats)

        return DiffAnalysis(
            raw_diff=diff,
            stats=stats,
            file_types=file_types,
            suggested_scope=suggested_scope,
            suggested_type=suggested_type
        )

    def _calculate_stats(self, diff: str) -> DiffStats:
        """
        Calculate diff statistics

        Args:
            diff: Raw git diff string

        Returns:
            DiffStats object
        """
        files_changed = 0
        insertions = 0
        deletions = 0
        files = []

        # Split by file headers
        file_chunks = re.split(r'^diff --git a/', diff, flags=re.MULTILINE)

        for chunk in file_chunks[1:]:  # Skip first empty chunk
            files_changed += 1

            # Extract filename
            match = re.search(r'^([\w/._-]+)', chunk)
            if match:
                files.append(match.group(1))

            # Count insertions and deletions
            for line in chunk.split('\n'):
                if line.startswith('+') and not line.startswith('+++'):
                    insertions += 1
                elif line.startswith('-') and not line.startswith('---'):
                    deletions += 1

        return DiffStats(
            files_changed=files_changed,
            insertions=insertions,
            deletions=deletions,
            files=files
        )

    def _extract_file_types(self, diff: str) -> List[str]:
        """
        Extract file extensions from diff

        Args:
            diff: Raw git diff string

        Returns:
            List of file extensions
        """
        extensions = set()

        # Match file extensions
        pattern = r'\.(\w+)'
        matches = re.findall(pattern, diff)

        extensions.update(matches)

        # Add special cases
        if 'Dockerfile' in diff:
            extensions.add('dockerfile')
        if 'Makefile' in diff:
            extensions.add('makefile')
        if any(ext in diff for ext in ['.yml', '.yaml']):
            extensions.add('yaml')

        return sorted(list(extensions))

    def _suggest_scope(self, diff: str) -> Optional[str]:
        """
        Suggest commit scope based on changed files

        Args:
            diff: Raw git diff string

        Returns:
            Suggested scope or None
        """
        scope_mappings = {
            "src/auth/": "auth",
            "src/ui/": "ui",
            "src/api/": "api",
            "src/utils/": "utils",
            "src/core/": "core",
            "tests/": "tests",
            "docs/": "docs",
            "config/": "config",
        }

        # Check for known paths
        for path, scope in scope_mappings.items():
            if path in diff:
                return scope

        return None

    def _suggest_type(self, diff: str, stats: DiffStats) -> Optional[CommitType]:
        """
        Suggest commit type based on diff content

        Args:
            diff: Raw git diff string
            stats: Diff statistics

        Returns:
            Suggested CommitType
        """
        # Check for test files
        if any('test' in f.lower() for f in stats.files):
            return CommitType.TEST

        # Check for documentation
        if any(ext in diff for ext in ['.md', '.txt', 'docs/']):
            if stats.insertions > 0 or stats.deletions > 0:
                return CommitType.DOCS

        # Check for common fix patterns
        fix_keywords = ['fix', 'bug', 'error', 'issue', 'patch']
        if any(keyword in diff.lower() for keyword in fix_keywords):
            return CommitType.FIX

        # Check for refactoring patterns
        refactor_keywords = ['refactor', 'restructure', 'reorganize', 'optimize']
        if any(keyword in diff.lower() for keyword in refactor_keywords):
            return CommitType.REFACTOR

        # Check for feature patterns
        feature_keywords = ['add', 'new', 'implement', 'create', 'feature']
        if any(keyword in diff.lower() for keyword in feature_keywords):
            return CommitType.FEAT

        # Default based on changes
        if stats.insertions > stats.deletions * 2:
            return CommitType.FEAT
        elif stats.deletions > stats.insertions:
            return CommitType.FIX
        else:
            return CommitType.CHORE
