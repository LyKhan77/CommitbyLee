"""Commit message generator using Qwen3:4B via Ollama"""

import logging
import re
from typing import Optional

from .ollama_client import OllamaClient
from .diff_analyzer import DiffAnalyzer
from .models.schemas import (
    CommitMessage,
    DiffAnalysis,
    Language,
    CommitStyle,
    CommitType
)
from .utils import clean_diff, chunk_diff_by_files

logger = logging.getLogger(__name__)


class CommitMessageGenerator:
    """
    Generate commit messages using Qwen3:4B via Ollama
    """

    def __init__(
        self,
        ollama_client: Optional[OllamaClient] = None,
        language: Language = Language.INDONESIAN
    ):
        """
        Initialize commit message generator

        Args:
            ollama_client: Ollama client instance
            language: Output language (Indonesian or English)
        """
        self.client = ollama_client or OllamaClient()
        self.language = language

    def generate(
        self,
        diff: str,
        analysis: Optional[DiffAnalysis] = None,
        style: CommitStyle = CommitStyle.CONVENTIONAL
    ) -> CommitMessage:
        """
        Generate commit message from diff

        Args:
            diff: Git diff string
            analysis: Diff analysis result (optional, will be generated if not provided)
            style: Commit message style

        Returns:
            CommitMessage object
        """
        if not diff:
            raise ValueError("Diff cannot be empty")

        # Analyze diff if not provided
        if not analysis:
            analyzer = DiffAnalyzer()
            analysis = analyzer.analyze_diff(diff)

        # Clean and chunk diff for better model performance
        cleaned_diff = clean_diff(diff)
        if analysis.stats.files_changed > 5:
            cleaned_diff = chunk_diff_by_files(cleaned_diff, max_files=5)
            logger.info(f"Chunked diff from {len(diff)} to {len(cleaned_diff)} characters")

        # Generate prompt based on language
        prompt = self._build_prompt(cleaned_diff, analysis)

        # Generate using Qwen3:4B
        try:
            response = self.client.generate(
                prompt=prompt,
                temperature=0.7,
                max_tokens=500
            )

            # If response is empty, use fallback based on analysis
            if not response or response.strip() == "":
                logger.warning("Empty response from LLM, using fallback")
                commit_msg = self._create_fallback_message(analysis)
            else:
                # Parse response
                commit_msg = self._parse_response(response, analysis)

            return commit_msg

        except Exception as e:
            logger.error(f"Failed to generate commit message: {e}")
            # Fallback to basic message
            logger.info("Using fallback message")
            return self._create_fallback_message(analysis)

    def _build_prompt(self, diff: str, analysis: DiffAnalysis) -> str:
        """
        Build prompt for Qwen3:4B

        Args:
            diff: Git diff string
            analysis: Diff analysis result

        Returns:
            Formatted prompt
        """
        if self.language == Language.INDONESIAN:
            return self._build_indonesian_prompt(diff, analysis)
        else:
            return self._build_english_prompt(diff, analysis)

    def _build_indonesian_prompt(self, diff: str, analysis: DiffAnalysis) -> str:
        """Build prompt in Indonesian"""
        prompt = f"""Buat pesan commit dalam format Conventional Commits untuk perubahan kode berikut:

FORMAT WAJIB:
type(scope): subject

subject harus deskriptif dan singkat.

Type yang boleh dipakai:
- feat: fitur baru
- fix: perbaikan bug
- docs: perubahan dokumentasi
- refactor: refactoring kode
- test: menambah/mengubah test
- chore: maintenance, update dependency, dll

Statistik:
- File berubah: {analysis.stats.files_changed}
- Insertions: +{analysis.stats.insertions}
- Deletions: -{analysis.stats.deletions}

Diff:
{diff}

PESAN COMMIT (hanya output, tanpa penjelasan):"""

        return prompt

    def _build_english_prompt(self, diff: str, analysis: DiffAnalysis) -> str:
        """Build prompt in English"""
        prompt = f"""Create a Conventional Commits message for the following code changes:

REQUIRED FORMAT:
type(scope): subject

Subject must be descriptive and concise.

Allowed types:
- feat: new feature
- fix: bug fix
- docs: documentation changes
- refactor: code refactoring
- test: adding/updating tests
- chore: maintenance, dependency updates, etc.

Statistics:
- Files changed: {analysis.stats.files_changed}
- Insertions: +{analysis.stats.insertions}
- Deletions: -{analysis.stats.deletions}

Diff:
{diff}

COMMIT MESSAGE (output only, no explanation):"""

        return prompt

    def _parse_response(self, response: str, analysis: DiffAnalysis) -> CommitMessage:
        """
        Parse Qwen3:4B response into CommitMessage

        Args:
            response: Generated text from Qwen3:4B
            analysis: Diff analysis result

        Returns:
            CommitMessage object
        """
        lines = response.strip().split('\n')

        # Parse first line as type(scope): subject
        first_line = lines[0].strip()

        # Extract type and scope
        type_match = re.match(r'^(\w+)(?:\(([^)]+)\))?:?\s*(.+)$', first_line)

        if type_match:
            commit_type_str = type_match.group(1).lower()
            scope = type_match.group(2)
            subject = type_match.group(3)

            # Map to CommitType enum
            try:
                commit_type = CommitType(commit_type_str)
            except ValueError:
                # Invalid type, default based on analysis
                commit_type = analysis.suggested_type or CommitType.CHORE

            # Extract body (remaining lines)
            body = None
            if len(lines) > 1:
                body_lines = [line.strip() for line in lines[1:] if line.strip()]
                if body_lines:
                    body = '\n'.join(body_lines)

            return CommitMessage(
                type=commit_type,
                scope=scope,
                subject=subject,
                body=body
            )
        else:
            # Fallback: use entire response as subject
            return CommitMessage(
                type=analysis.suggested_type or CommitType.CHORE,
                scope=analysis.suggested_scope,
                subject=first_line
            )

    def set_language(self, language: Language):
        """
        Set output language

        Args:
            language: Language to use
        """
        self.language = language
        logger.info(f"Language set to {language.value}")

    def _create_fallback_message(self, analysis: DiffAnalysis) -> CommitMessage:
        """
        Create fallback commit message based on diff analysis

        Args:
            analysis: Diff analysis result

        Returns:
            CommitMessage object
        """
        commit_type = analysis.suggested_type or CommitType.CHORE
        scope = analysis.suggested_scope

        # Generate subject based on language and stats
        if self.language == Language.INDONESIAN:
            if commit_type == CommitType.FEAT:
                subject = f"tambahkan fitur pada {scope if scope else 'beberapa file'}"
            elif commit_type == CommitType.FIX:
                subject = f"perbaiki bug pada {scope if scope else 'beberapa file'}"
            elif commit_type == CommitType.DOCS:
                subject = "update dokumentasi"
            elif commit_type == CommitType.REFACTOR:
                subject = f"refactoring kode pada {scope if scope else 'beberapa file'}"
            elif commit_type == CommitType.TEST:
                subject = "update test"
            else:
                subject = f"update {scope if scope else 'file'}"
        else:  # English
            if commit_type == CommitType.FEAT:
                subject = f"add feature to {scope if scope else 'files'}"
            elif commit_type == CommitType.FIX:
                subject = f"fix bug in {scope if scope else 'files'}"
            elif commit_type == CommitType.DOCS:
                subject = "update documentation"
            elif commit_type == CommitType.REFACTOR:
                subject = f"refactor code in {scope if scope else 'files'}"
            elif commit_type == CommitType.TEST:
                subject = "update tests"
            else:
                subject = f"update {scope if scope else 'files'}"

        # Add stats info to body
        if self.language == Language.INDONESIAN:
            body = f"{analysis.stats.files_changed} file berubah, +{analysis.stats.insertions}, -{analysis.stats.deletions}"
        else:
            body = f"{analysis.stats.files_changed} file(s) changed, +{analysis.stats.insertions}, -{analysis.stats.deletions}"

        return CommitMessage(
            type=commit_type,
            scope=scope,
            subject=subject,
            body=body
        )
