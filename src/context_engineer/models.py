"""Data models for context engineering file management."""

from enum import Enum
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field


class FileStatus(str, Enum):
    """Status of a context engineering file."""

    FOUND = "found"
    MISSING = "missing"


class ContextFile(str, Enum):
    """Known context engineering files."""

    CLAUDE_MD = "CLAUDE.md"
    PLANNING_MD = "PLANNING.md"
    TASK_MD = "TASK.md"
    INITIAL_MD = "INITIAL.md"


CONTEXT_DIRS = [".claude", "PRPs", "examples"]


class ContextFileStatus(BaseModel):
    """Status of a single context engineering file.

    Args:
        name: File name (e.g., CLAUDE.md).
        status: Whether the file was found or is missing.
        path: Absolute path to the file.
        line_count: Number of lines if found.
    """

    name: str
    status: FileStatus
    path: Path
    line_count: int = 0


class ContextDirStatus(BaseModel):
    """Status of a context engineering directory.

    Args:
        name: Directory name (e.g., .claude).
        status: Whether the directory was found or is missing.
        path: Absolute path to the directory.
        item_count: Number of items inside if found.
    """

    name: str
    status: FileStatus
    path: Path
    item_count: int = 0


class ScanResult(BaseModel):
    """Result of scanning a workspace for context engineering files.

    Args:
        workspace_path: Path to the scanned workspace.
        files: Status of each context file.
        dirs: Status of each context directory.
        score: Number of items found out of total.
        total: Total number of expected items.
    """

    workspace_path: Path
    files: list[ContextFileStatus] = Field(default_factory=list)
    dirs: list[ContextDirStatus] = Field(default_factory=list)
    score: int = 0
    total: int = 7


class ValidationCheck(BaseModel):
    """A single validation check result.

    Args:
        rule: Description of the validation rule.
        passed: Whether the check passed.
        severity: 'error', 'warning', or 'info'.
        message: Optional detail message.
    """

    rule: str
    passed: bool
    severity: str = "error"
    message: Optional[str] = None


class ValidationResult(BaseModel):
    """Result of validating a context engineering file.

    Args:
        file_name: Name of the validated file.
        file_path: Path to the validated file.
        checks: List of validation checks performed.
        score: Number of checks passed.
        total: Total number of checks.
    """

    file_name: str
    file_path: Path
    checks: list[ValidationCheck] = Field(default_factory=list)
    score: int = 0
    total: int = 0
