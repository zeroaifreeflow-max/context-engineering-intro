"""Shared fixtures for context engineer tests."""

import pytest
from pathlib import Path


@pytest.fixture
def tmp_workspace(tmp_path: Path) -> Path:
    """Create a temporary workspace directory.

    Args:
        tmp_path: Pytest-provided temporary directory.

    Returns:
        Path: Path to the temporary workspace.
    """
    return tmp_path


@pytest.fixture
def full_workspace(tmp_path: Path) -> Path:
    """Create a workspace with all context engineering files present.

    Args:
        tmp_path: Pytest-provided temporary directory.

    Returns:
        Path: Path to the fully populated workspace.
    """
    # Create context files
    (tmp_path / "CLAUDE.md").write_text(
        "# Project Rules\n\n"
        "## Testing\n- Use pytest\n\n"
        "## Style & Conventions\n- Follow PEP8\n- Use type hints\n"
    )
    (tmp_path / "PLANNING.md").write_text(
        "# PLANNING\n\n"
        "## Architecture\n```\nsrc/\n  main.py\n```\n\n"
        "## Tech Stack\n- Python 3.11\n- FastAPI\n"
    )
    (tmp_path / "TASK.md").write_text(
        "# TASK.md\n\n"
        "## Active Tasks\n- Task 1 (2026-03-07)\n\n"
        "## Completed Tasks\n- Setup (2026-03-01)\n"
    )
    (tmp_path / "INITIAL.md").write_text(
        "## FEATURE:\nBuild a REST API for user management\n\n"
        "## EXAMPLES:\nSee `examples/api.py`\n\n"
        "## DOCUMENTATION:\nhttps://fastapi.tiangolo.com\n\n"
        "## OTHER CONSIDERATIONS:\nUse JWT auth\n"
    )

    # Create directories
    commands_dir = tmp_path / ".claude" / "commands"
    commands_dir.mkdir(parents=True)
    (commands_dir / "test-cmd.md").write_text("# Test Command\n")
    (commands_dir / "another-cmd.md").write_text("# Another\n")

    prps_dir = tmp_path / "PRPs"
    prps_dir.mkdir()
    (prps_dir / "feature-1.md").write_text("# PRP 1\n")

    examples_dir = tmp_path / "examples"
    examples_dir.mkdir()
    (examples_dir / "api.py").write_text("# example\n")

    return tmp_path


@pytest.fixture
def empty_workspace(tmp_path: Path) -> Path:
    """Create an empty workspace with no context files.

    Args:
        tmp_path: Pytest-provided temporary directory.

    Returns:
        Path: Path to the empty workspace.
    """
    return tmp_path
