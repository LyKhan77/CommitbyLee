"""Utility functions"""

import re
from typing import Optional, List


def clean_diff(diff: str, max_length: int = 5000) -> str:
    """
    Clean and truncate diff if necessary

    Args:
        diff: Raw diff string
        max_length: Maximum length (reduced to 5000 for better model performance)

    Returns:
        Cleaned diff
    """
    # Remove sensitive data patterns (basic)
    # Remove API keys, passwords, tokens
    sensitive_patterns = [
        r'password["\']?\s*[:=]\s*["\']?[^"\'\s]+',
        r'api_key["\']?\s*[:=]\s*["\']?[^"\'\s]+',
        r'token["\']?\s*[:=]\s*["\']?[^"\'\s]+',
        r'secret["\']?\s*[:=]\s*["\']?[^"\'\s]+',
    ]

    cleaned = diff
    for pattern in sensitive_patterns:
        cleaned = re.sub(pattern, '[REDACTED]', cleaned, flags=re.IGNORECASE)

    # Truncate if too long
    if len(cleaned) > max_length:
        # Try to truncate at a file boundary
        lines = cleaned.split('\n')
        result = []
        current_length = 0

        for line in lines:
            if current_length + len(line) > max_length:
                break
            result.append(line)
            current_length += len(line) + 1  # +1 for newline

        cleaned = '\n'.join(result)
        if len(cleaned) < max_length:
            cleaned += "\n\n... (truncated for brevity)"

    return cleaned


def chunk_diff_by_files(diff: str, max_files: int = 5) -> str:
    """
    Chunk diff to include only first N files for better model performance

    Args:
        diff: Raw diff string
        max_files: Maximum number of files to include

    Returns:
        Chunked diff
    """
    # Split by file headers
    file_chunks = re.split(r'^diff --git a/', diff, flags=re.MULTILINE)

    # Keep only first N files (plus the initial empty chunk)
    if len(file_chunks) > max_files + 1:
        selected_chunks = file_chunks[:max_files + 1]
        result = 'diff --git a/'.join(selected_chunks)
        result += f"\n\n... ({len(file_chunks) - max_files - 1} more files omitted for brevity)"
        return result

    return diff


def validate_commit_message(message: str) -> bool:
    """
    Validate commit message format

    Args:
        message: Commit message string

    Returns:
        True if valid, False otherwise
    """
    # Check conventional commit format
    pattern = r'^(feat|fix|docs|style|refactor|test|chore|perf|ci|build)(\(.+\))?\s*:\s*.+'

    return bool(re.match(pattern, message))


def truncate_subject(subject: str, max_length: int = 72) -> str:
    """
    Truncate subject to max length

    Args:
        subject: Subject string
        max_length: Maximum length

    Returns:
        Truncated subject
    """
    if len(subject) <= max_length:
        return subject

    return subject[:max_length - 3] + "..."


def detect_breaking_change(diff: str) -> bool:
    """
    Detect if changes are breaking

    Args:
        diff: Git diff string

    Returns:
        True if breaking change detected
    """
    breaking_keywords = [
        'BREAKING CHANGE:',
        'breaking change',
        '!!:',  # Conventional commits breaking change indicator
    ]

    diff_lower = diff.lower()
    return any(keyword.lower() in diff_lower for keyword in breaking_keywords)
