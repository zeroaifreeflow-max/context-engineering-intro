"""Validator module for checking context engineering file quality."""

import re
from pathlib import Path

from src.context_engineer.models import (
    ContextFile,
    ValidationCheck,
    ValidationResult,
)


def _read_file_content(file_path: Path) -> str | None:
    """Read file content safely.

    Args:
        file_path: Path to the file.

    Returns:
        str | None: File content or None if unreadable.
    """
    try:
        return file_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None


def _has_section(content: str, heading: str) -> bool:
    """Check if markdown content has a section with the given heading.

    Args:
        content: Markdown content.
        heading: Heading text to search for (case-insensitive).

    Returns:
        bool: True if the section exists.
    """
    pattern = rf"^#+\s+.*{re.escape(heading)}.*$"
    return bool(re.search(pattern, content, re.MULTILINE | re.IGNORECASE))


def _is_placeholder_only(content: str) -> bool:
    """Check if content contains only placeholder text.

    Args:
        content: File content to check.

    Returns:
        bool: True if content appears to be placeholder-only.
    """
    placeholder_patterns = [
        r"\[Insert .+\]",
        r"\[Provide .+\]",
        r"\[List .+\]",
        r"\[Any .+\]",
        r"\[PLACEHOLDER\]",
        r"\[Describe .+\]",
    ]
    lines = [
        line.strip()
        for line in content.splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]
    if not lines:
        return True

    placeholder_count = sum(
        1
        for line in lines
        if any(re.search(p, line) for p in placeholder_patterns)
    )
    # Reason: If more than half of non-heading lines are placeholders, treat as placeholder-only
    return placeholder_count > len(lines) / 2


def validate_claude_md(file_path: Path) -> ValidationResult:
    """Validate a CLAUDE.md file for quality.

    Args:
        file_path: Path to CLAUDE.md.

    Returns:
        ValidationResult: Validation results with checks.
    """
    result = ValidationResult(
        file_name="CLAUDE.md",
        file_path=file_path,
    )
    content = _read_file_content(file_path)
    if content is None:
        result.checks.append(
            ValidationCheck(
                rule="File is readable",
                passed=False,
                message="Could not read file",
            )
        )
        result.total = 1
        return result

    line_count = len(content.splitlines())

    checks = [
        ValidationCheck(
            rule="Contains project-specific rules",
            passed=not _is_placeholder_only(content),
            message="File contains only placeholder text"
            if _is_placeholder_only(content)
            else None,
        ),
        ValidationCheck(
            rule="Under 80 lines (concise)",
            passed=line_count <= 80,
            severity="warning",
            message=f"{line_count} lines (recommended: under 80)"
            if line_count > 80
            else None,
        ),
        ValidationCheck(
            rule="Testing requirements present",
            passed=_has_section(content, "test")
            or "test" in content.lower(),
        ),
        ValidationCheck(
            rule="Code style conventions present",
            passed=_has_section(content, "style")
            or _has_section(content, "convention")
            or "style" in content.lower(),
        ),
    ]

    result.checks = checks
    result.total = len(checks)
    result.score = sum(1 for c in checks if c.passed)
    return result


def validate_planning_md(file_path: Path) -> ValidationResult:
    """Validate a PLANNING.md file for quality.

    Args:
        file_path: Path to PLANNING.md.

    Returns:
        ValidationResult: Validation results with checks.
    """
    result = ValidationResult(
        file_name="PLANNING.md",
        file_path=file_path,
    )
    content = _read_file_content(file_path)
    if content is None:
        result.checks.append(
            ValidationCheck(
                rule="File is readable",
                passed=False,
                message="Could not read file",
            )
        )
        result.total = 1
        return result

    line_count = len(content.splitlines())

    checks = [
        ValidationCheck(
            rule="Contains architecture description",
            passed=_has_section(content, "architect")
            or _has_section(content, "structure"),
        ),
        ValidationCheck(
            rule="Contains tech stack information",
            passed=_has_section(content, "tech")
            or _has_section(content, "stack")
            or "tech stack" in content.lower(),
        ),
        ValidationCheck(
            rule="Under 120 lines",
            passed=line_count <= 120,
            severity="warning",
            message=f"{line_count} lines (recommended: under 120)"
            if line_count > 120
            else None,
        ),
        ValidationCheck(
            rule="References actual file paths",
            passed=bool(re.search(r"[`/]\w+\.\w+", content))
            or bool(re.search(r"`[^`]+/[^`]+`", content)),
        ),
    ]

    result.checks = checks
    result.total = len(checks)
    result.score = sum(1 for c in checks if c.passed)
    return result


def validate_task_md(file_path: Path) -> ValidationResult:
    """Validate a TASK.md file for quality.

    Args:
        file_path: Path to TASK.md.

    Returns:
        ValidationResult: Validation results with checks.
    """
    result = ValidationResult(
        file_name="TASK.md",
        file_path=file_path,
    )
    content = _read_file_content(file_path)
    if content is None:
        result.checks.append(
            ValidationCheck(
                rule="File is readable",
                passed=False,
                message="Could not read file",
            )
        )
        result.total = 1
        return result

    checks = [
        ValidationCheck(
            rule="Has Active Tasks section",
            passed=_has_section(content, "active")
            or _has_section(content, "current")
            or _has_section(content, "in progress"),
        ),
        ValidationCheck(
            rule="Has Completed Tasks section",
            passed=_has_section(content, "completed")
            or _has_section(content, "done"),
        ),
        ValidationCheck(
            rule="Tasks have dates",
            passed=bool(re.search(r"\d{4}-\d{2}-\d{2}", content)),
            severity="warning",
            message="No dates found in tasks"
            if not re.search(r"\d{4}-\d{2}-\d{2}", content)
            else None,
        ),
    ]

    result.checks = checks
    result.total = len(checks)
    result.score = sum(1 for c in checks if c.passed)
    return result


def validate_initial_md(file_path: Path) -> ValidationResult:
    """Validate an INITIAL.md file for quality.

    Args:
        file_path: Path to INITIAL.md.

    Returns:
        ValidationResult: Validation results with checks.
    """
    result = ValidationResult(
        file_name="INITIAL.md",
        file_path=file_path,
    )
    content = _read_file_content(file_path)
    if content is None:
        result.checks.append(
            ValidationCheck(
                rule="File is readable",
                passed=False,
                message="Could not read file",
            )
        )
        result.total = 1
        return result

    checks = [
        ValidationCheck(
            rule="Has FEATURE section",
            passed=_has_section(content, "feature"),
        ),
        ValidationCheck(
            rule="Has EXAMPLES section",
            passed=_has_section(content, "example"),
        ),
        ValidationCheck(
            rule="Has DOCUMENTATION section",
            passed=_has_section(content, "documentation"),
        ),
        ValidationCheck(
            rule="Not placeholder-only content",
            passed=not _is_placeholder_only(content),
            severity="warning",
            message="File contains mostly placeholder text"
            if _is_placeholder_only(content)
            else None,
        ),
    ]

    result.checks = checks
    result.total = len(checks)
    result.score = sum(1 for c in checks if c.passed)
    return result


# Mapping of context files to their validator functions
_VALIDATORS = {
    ContextFile.CLAUDE_MD: validate_claude_md,
    ContextFile.PLANNING_MD: validate_planning_md,
    ContextFile.TASK_MD: validate_task_md,
    ContextFile.INITIAL_MD: validate_initial_md,
}


def validate_file(file_path: str | Path) -> ValidationResult:
    """Validate a single context engineering file.

    Args:
        file_path: Path to the file to validate.

    Returns:
        ValidationResult: Validation results.

    Raises:
        ValueError: If the file is not a known context engineering file.
    """
    fp = Path(file_path)
    try:
        ctx_file = ContextFile(fp.name)
    except ValueError:
        raise ValueError(
            f"Unknown context file: {fp.name}. "
            f"Expected one of: {[f.value for f in ContextFile]}"
        )

    validator = _VALIDATORS[ctx_file]
    return validator(fp)


def validate_workspace(workspace_path: str | Path = ".") -> list[ValidationResult]:
    """Validate all context engineering files in a workspace.

    Args:
        workspace_path: Path to the workspace directory.

    Returns:
        list[ValidationResult]: Validation results for each found file.
    """
    ws = Path(workspace_path).resolve()
    results = []

    for ctx_file in ContextFile:
        fp = ws / ctx_file.value
        if fp.is_file():
            validator = _VALIDATORS[ctx_file]
            results.append(validator(fp))

    return results


def format_validation_result(result: ValidationResult) -> str:
    """Format a ValidationResult into a human-readable string.

    Args:
        result: The validation result to format.

    Returns:
        str: Formatted string representation.
    """
    lines = [f"Validating: {result.file_name}"]

    for check in result.checks:
        if check.passed:
            lines.append(f"  Passed: {check.rule}")
        elif check.severity == "warning":
            msg = f"  Warning: {check.rule}"
            if check.message:
                msg += f" - {check.message}"
            lines.append(msg)
        else:
            msg = f"  Failed: {check.rule}"
            if check.message:
                msg += f" - {check.message}"
            lines.append(msg)

    lines.append(f"  Score: {result.score}/{result.total}")
    return "\n".join(lines)
