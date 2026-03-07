"""Tests for the exporter module."""

from pathlib import Path

import pytest

from src.context_engineer.exporter import export_bundle


class TestExportBundle:
    """Tests for export_bundle function."""

    def test_export_full_workspace(self, full_workspace: Path) -> None:
        """Exporting a full workspace should create a bundle with all files."""
        output = export_bundle(full_workspace)

        assert output.exists()
        content = output.read_text(encoding="utf-8")
        assert "CLAUDE.md" in content
        assert "PLANNING.md" in content
        assert "TASK.md" in content
        assert "INITIAL.md" in content
        assert "7/7" in content

    def test_export_empty_workspace(self, empty_workspace: Path) -> None:
        """Exporting an empty workspace should note missing files."""
        output = export_bundle(empty_workspace)

        assert output.exists()
        content = output.read_text(encoding="utf-8")
        assert "not found" in content.lower()
        assert "0/7" in content

    def test_export_custom_output_path(self, full_workspace: Path) -> None:
        """Export should write to the specified output path."""
        custom_path = full_workspace / "my-bundle.md"
        output = export_bundle(full_workspace, output_path=custom_path)

        assert output == custom_path
        assert custom_path.exists()

    def test_export_default_filename_format(self, full_workspace: Path) -> None:
        """Default output filename should contain 'context-bundle' and date."""
        output = export_bundle(full_workspace)

        assert "context-bundle-" in output.name
        assert output.suffix == ".md"

    def test_export_includes_file_content(self, full_workspace: Path) -> None:
        """Bundle should include the actual content of context files."""
        output = export_bundle(full_workspace)

        content = output.read_text(encoding="utf-8")
        # Reason: CLAUDE.md in full_workspace fixture contains "pytest"
        assert "pytest" in content.lower()
