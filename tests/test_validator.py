"""Tests for the validator module."""

from pathlib import Path

import pytest

from src.context_engineer.validator import (
    format_validation_result,
    validate_file,
    validate_workspace,
)


class TestValidateClaudeMd:
    """Tests for CLAUDE.md validation."""

    def test_valid_claude_md(self, full_workspace: Path) -> None:
        """A well-formed CLAUDE.md should pass all checks."""
        result = validate_file(full_workspace / "CLAUDE.md")

        assert result.file_name == "CLAUDE.md"
        assert result.score == result.total

    def test_placeholder_only_claude_md(self, tmp_path: Path) -> None:
        """A placeholder-only CLAUDE.md should fail the specificity check."""
        (tmp_path / "CLAUDE.md").write_text(
            "# Rules\n\n[Insert your rules here]\n[Provide your conventions]\n"
        )
        result = validate_file(tmp_path / "CLAUDE.md")

        specificity = next(
            c for c in result.checks if "project-specific" in c.rule
        )
        assert not specificity.passed

    def test_long_claude_md_warns(self, tmp_path: Path) -> None:
        """A CLAUDE.md over 80 lines should trigger a warning."""
        content = "# Rules\n" + "\n".join(
            [f"- Rule {i}" for i in range(100)]
        )
        (tmp_path / "CLAUDE.md").write_text(content)
        result = validate_file(tmp_path / "CLAUDE.md")

        length_check = next(c for c in result.checks if "80 lines" in c.rule)
        assert not length_check.passed
        assert length_check.severity == "warning"


class TestValidatePlanningMd:
    """Tests for PLANNING.md validation."""

    def test_valid_planning_md(self, full_workspace: Path) -> None:
        """A well-formed PLANNING.md should pass all checks."""
        result = validate_file(full_workspace / "PLANNING.md")

        assert result.score == result.total

    def test_missing_architecture(self, tmp_path: Path) -> None:
        """PLANNING.md without architecture section should fail."""
        (tmp_path / "PLANNING.md").write_text("# Plan\nSome notes\n")
        result = validate_file(tmp_path / "PLANNING.md")

        arch_check = next(c for c in result.checks if "architecture" in c.rule.lower())
        assert not arch_check.passed


class TestValidateTaskMd:
    """Tests for TASK.md validation."""

    def test_valid_task_md(self, full_workspace: Path) -> None:
        """A well-formed TASK.md should pass all checks."""
        result = validate_file(full_workspace / "TASK.md")

        assert result.score == result.total

    def test_no_dates_warns(self, tmp_path: Path) -> None:
        """TASK.md without dates should trigger a warning."""
        (tmp_path / "TASK.md").write_text(
            "# Tasks\n## Active Tasks\n- Do something\n## Completed Tasks\n"
        )
        result = validate_file(tmp_path / "TASK.md")

        date_check = next(c for c in result.checks if "date" in c.rule.lower())
        assert not date_check.passed
        assert date_check.severity == "warning"


class TestValidateInitialMd:
    """Tests for INITIAL.md validation."""

    def test_valid_initial_md(self, full_workspace: Path) -> None:
        """A well-formed INITIAL.md should pass all checks."""
        result = validate_file(full_workspace / "INITIAL.md")

        assert result.score == result.total

    def test_placeholder_initial_md(self, tmp_path: Path) -> None:
        """An INITIAL.md with only placeholders should warn."""
        (tmp_path / "INITIAL.md").write_text(
            "## FEATURE:\n[Insert your feature here]\n\n"
            "## EXAMPLES:\n[Provide examples]\n\n"
            "## DOCUMENTATION:\n[List documentation]\n"
        )
        result = validate_file(tmp_path / "INITIAL.md")

        placeholder_check = next(
            c for c in result.checks if "placeholder" in c.rule.lower()
        )
        assert not placeholder_check.passed


class TestValidateUnknownFile:
    """Tests for unknown file validation."""

    def test_unknown_file_raises(self, tmp_path: Path) -> None:
        """Validating an unknown file type should raise ValueError."""
        (tmp_path / "RANDOM.md").write_text("# Random\n")

        with pytest.raises(ValueError, match="Unknown context file"):
            validate_file(tmp_path / "RANDOM.md")


class TestValidateWorkspace:
    """Tests for workspace-level validation."""

    def test_full_workspace_validates_all(self, full_workspace: Path) -> None:
        """All files should be validated in a full workspace."""
        results = validate_workspace(full_workspace)

        assert len(results) == 4
        names = [r.file_name for r in results]
        assert "CLAUDE.md" in names
        assert "PLANNING.md" in names
        assert "TASK.md" in names
        assert "INITIAL.md" in names

    def test_empty_workspace_no_results(self, empty_workspace: Path) -> None:
        """No results should be returned for an empty workspace."""
        results = validate_workspace(empty_workspace)

        assert len(results) == 0


class TestFormatValidationResult:
    """Tests for format_validation_result."""

    def test_format_includes_file_name(self, full_workspace: Path) -> None:
        """Formatted output should include the file name."""
        result = validate_file(full_workspace / "CLAUDE.md")
        output = format_validation_result(result)

        assert "CLAUDE.md" in output

    def test_format_includes_score(self, full_workspace: Path) -> None:
        """Formatted output should include the score."""
        result = validate_file(full_workspace / "CLAUDE.md")
        output = format_validation_result(result)

        assert f"{result.score}/{result.total}" in output
