"""Exporter module for bundling context engineering files."""

from datetime import datetime
from pathlib import Path

from src.context_engineer.models import ContextFile, FileStatus
from src.context_engineer.scanner import scan_workspace


def export_bundle(
    workspace_path: str | Path = ".",
    output_path: str | Path | None = None,
) -> Path:
    """Export all context engineering files as a single markdown bundle.

    Collects CLAUDE.md, PLANNING.md, TASK.md, and INITIAL.md from the
    workspace and combines them into a portable bundle file.

    Args:
        workspace_path: Path to the workspace directory.
        output_path: Output file path. Defaults to
            context-bundle-YYYY-MM-DD.md in the workspace.

    Returns:
        Path: Path to the created bundle file.
    """
    ws = Path(workspace_path).resolve()
    today = datetime.now().strftime("%Y-%m-%d")

    if output_path is None:
        output_path = ws / f"context-bundle-{today}.md"
    else:
        output_path = Path(output_path).resolve()

    scan = scan_workspace(ws)

    lines = [
        f"# Context Engineering Bundle",
        f"",
        f"- **Workspace**: {ws}",
        f"- **Date**: {today}",
        f"- **Score**: {scan.score}/{scan.total}",
        f"",
        f"---",
        f"",
    ]

    for ctx_file in ContextFile:
        file_path = ws / ctx_file.value
        lines.append(f"## {ctx_file.value}")
        lines.append("")

        if file_path.is_file():
            content = file_path.read_text(encoding="utf-8")
            lines.append(content)
        else:
            lines.append("*File not found in workspace.*")

        lines.append("")
        lines.append("---")
        lines.append("")

    found_files = [
        f.name for f in scan.files if f.status == FileStatus.FOUND
    ]
    missing_files = [
        f.name for f in scan.files if f.status == FileStatus.MISSING
    ]

    lines.append("## Bundle Summary")
    lines.append("")
    lines.append(f"- **Files included**: {', '.join(found_files) or 'none'}")
    lines.append(f"- **Files missing**: {', '.join(missing_files) or 'none'}")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path
