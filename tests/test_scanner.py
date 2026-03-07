"""Tests for the scanner module."""

from pathlib import Path

import pytest

from src.context_engineer.models import FileStatus
from src.context_engineer.scanner import (
    format_scan_result,
    scan_workspace,
)


class TestScanWorkspace:
    """Tests for scan_workspace function."""

    def test_full_workspace_all_found(self, full_workspace: Path) -> None:
        """All context items should be found in a fully populated workspace."""
        result = scan_workspace(full_workspace)

        assert result.score == 7
        assert result.total == 7
        assert len(result.files) == 4
        assert len(result.dirs) == 3
        assert all(f.status == FileStatus.FOUND for f in result.files)
        assert all(d.status == FileStatus.FOUND for d in result.dirs)

    def test_empty_workspace_all_missing(self, empty_workspace: Path) -> None:
        """All context items should be missing in an empty workspace."""
        result = scan_workspace(empty_workspace)

        assert result.score == 0
        assert result.total == 7
        assert all(f.status == FileStatus.MISSING for f in result.files)
        assert all(d.status == FileStatus.MISSING for d in result.dirs)

    def test_partial_workspace(self, tmp_path: Path) -> None:
        """Only present files should be marked as found."""
        (tmp_path / "CLAUDE.md").write_text("# Rules\n")
        (tmp_path / "TASK.md").write_text("# Tasks\n")

        result = scan_workspace(tmp_path)

        assert result.score == 2
        found_names = [f.name for f in result.files if f.status == FileStatus.FOUND]
        assert "CLAUDE.md" in found_names
        assert "TASK.md" in found_names

    def test_line_count_tracked(self, full_workspace: Path) -> None:
        """Found files should have their line count recorded."""
        result = scan_workspace(full_workspace)

        claude_file = next(f for f in result.files if f.name == "CLAUDE.md")
        assert claude_file.line_count > 0

    def test_command_count(self, full_workspace: Path) -> None:
        """The .claude directory should count commands correctly."""
        result = scan_workspace(full_workspace)

        claude_dir = next(d for d in result.dirs if d.name == ".claude")
        assert claude_dir.item_count == 2

    def test_nonexistent_path(self, tmp_path: Path) -> None:
        """Scanning a nonexistent subdir should return all missing."""
        result = scan_workspace(tmp_path / "does-not-exist")

        assert result.score == 0


class TestFormatScanResult:
    """Tests for format_scan_result function."""

    def test_format_includes_score(self, full_workspace: Path) -> None:
        """Formatted output should include the score line."""
        result = scan_workspace(full_workspace)
        output = format_scan_result(result)

        assert "7/7" in output
        assert "Score" in output

    def test_format_shows_missing(self, empty_workspace: Path) -> None:
        """Formatted output should show 'Missing' for absent files."""
        result = scan_workspace(empty_workspace)
        output = format_scan_result(result)

        assert "Missing" in output
        assert "0/7" in output

    def test_format_shows_line_count(self, full_workspace: Path) -> None:
        """Formatted output should show line counts for found files."""
        result = scan_workspace(full_workspace)
        output = format_scan_result(result)

        assert "lines" in output
