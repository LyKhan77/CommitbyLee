"""Commit message formatters"""

from .models.schemas import CommitMessage, CommitStyle


def format_commit_message(message: CommitMessage, style: CommitStyle) -> str:
    """
    Format commit message according to style

    Args:
        message: CommitMessage object
        style: Desired style

    Returns:
        Formatted commit message string
    """
    if style == CommitStyle.EMOJI:
        return message.format_emoji()
    elif style == CommitStyle.SIMPLE:
        return message.format_simple()
    else:  # CONVENTIONAL
        return message.format_conventional()
