"""Scanner module for detecting context engineering files in a workspace."""

from pathlib import Path

from src.context_engineer.models import (
    CONTEXT_DIRS,
    ContextDirStatus,
    ContextFile,
    ContextFileStatus,
    FileStatus,
    ScanResult,
)


def _count_lines(file_path: Path) -> int:
    """Count the number of lines in a file.

    Args:
        file_path: Path to the file.

    Returns:
        int: Number of lines in the file.
    """
    try:
        return len(file_path.read_text(encoding="utf-8").splitlines())
    except (OSError, UnicodeDecodeError):
        return 0


def _count_items(dir_path: Path) -> int:
    """Count relevant items inside a context directory.

    Args:
        dir_path: Path to the directory.

    Returns:
        int: Number of relevant items found.
    """
    if not dir_path.is_dir():
        return 0

    count = 0
    for item in dir_path.rglob("*"):
        if item.is_file() and not item.name.startswith("."):
            count += 1
    return count


def _count_commands(claude_dir: Path) -> int:
    """Count Claude Code commands in .claude/commands/.

    Args:
        claude_dir: Path to the .claude directory.

    Returns:
        int: Number of command files found.
    """
    commands_dir = claude_dir / "commands"
    if not commands_dir.is_dir():
        return 0
    return len(list(commands_dir.glob("*.md")))


def scan_workspace(workspace_path: str | Path = ".") -> ScanResult:
    """Scan a workspace directory for context engineering files.

    Checks for the presence of CLAUDE.md, PLANNING.md, TASK.md,
    INITIAL.md, .claude/, PRPs/, and examples/ directories.

    Args:
        workspace_path: Path to the workspace directory to scan.

    Returns:
        ScanResult: Detailed scan results with file and directory statuses.
    """
    ws = Path(workspace_path).resolve()
    result = ScanResult(workspace_path=ws)

    # Scan context files
    for ctx_file in ContextFile:
        file_path = ws / ctx_file.value
        if file_path.is_file():
            result.files.append(
                ContextFileStatus(
                    name=ctx_file.value,
                    status=FileStatus.FOUND,
                    path=file_path,
                    line_count=_count_lines(file_path),
                )
            )
        else:
            result.files.append(
                ContextFileStatus(
                    name=ctx_file.value,
                    status=FileStatus.MISSING,
                    path=file_path,
                )
            )

    # Scan context directories
    for dir_name in CONTEXT_DIRS:
        dir_path = ws / dir_name
        if dir_path.is_dir():
            if dir_name == ".claude":
                item_count = _count_commands(dir_path)
            else:
                item_count = _count_items(dir_path)
            result.dirs.append(
                ContextDirStatus(
                    name=dir_name,
                    status=FileStatus.FOUND,
                    path=dir_path,
                    item_count=item_count,
                )
            )
        else:
            result.dirs.append(
                ContextDirStatus(
                    name=dir_name,
                    status=FileStatus.MISSING,
                    path=dir_path,
                )
            )

    # Calculate score
    result.score = sum(
        1 for f in result.files if f.status == FileStatus.FOUND
    ) + sum(1 for d in result.dirs if d.status == FileStatus.FOUND)

    return result


def format_scan_result(result: ScanResult) -> str:
    """Format a ScanResult into a human-readable string.

    Args:
        result: The scan result to format.

    Returns:
        str: Formatted string representation.
    """
    lines = [
        f"Context Engineering Status: {result.workspace_path}",
        "-" * 50,
    ]

    for f in result.files:
        if f.status == FileStatus.FOUND:
            lines.append(f"  {f.name:<16} Found ({f.line_count} lines)")
        else:
            lines.append(f"  {f.name:<16} Missing")

    for d in result.dirs:
        if d.status == FileStatus.FOUND:
            label = "commands" if d.name == ".claude" else "files"
            lines.append(
                f"  {d.name + '/':<16} Found ({d.item_count} {label})"
            )
        else:
            lines.append(f"  {d.name + '/':<16} Missing")

    lines.append("-" * 50)
    lines.append(f"Score: {result.score}/{result.total} context items present")

    return "\n".join(lines)
