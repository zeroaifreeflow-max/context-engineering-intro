# Context Engineer — File Management Skill

Manage context engineering files across workspace repos. Scan, create, validate, update, and audit CLAUDE.md, PLANNING.md, TASK.md, and INITIAL.md files.

## Command: $ARGUMENTS

## Available Actions

Parse the first word of `$ARGUMENTS` to determine the action:

### `scan [path]` — Scan a workspace for context files
Scan the given directory (default: current directory) and report which context engineering files exist, which are missing, and their quality.

Steps:
1. Check for existence of: CLAUDE.md, PLANNING.md, TASK.md, INITIAL.md
2. Check for `.claude/commands/` directory and list available commands
3. Check for `PRPs/` directory and any existing PRPs
4. Check for `examples/` directory
5. Report status with a clear summary table

Output format:
```
Context Engineering Status: [path]
─────────────────────────────────────
  CLAUDE.md      ✅ Found (XX lines)  |  ❌ Missing
  PLANNING.md    ✅ Found (XX lines)  |  ❌ Missing
  TASK.md        ✅ Found (XX lines)  |  ❌ Missing
  INITIAL.md     ✅ Found (XX lines)  |  ❌ Missing
  .claude/       ✅ Found (N commands) |  ❌ Missing
  PRPs/          ✅ Found (N PRPs)    |  ❌ Missing
  examples/      ✅ Found (N files)   |  ❌ Missing
─────────────────────────────────────
Score: X/7 context files present
```

### `init [path]` — Initialize context engineering in a workspace
Create all missing context engineering files using templates from the CE Starter Kits.

Steps:
1. Run `scan` first to determine what exists
2. Ask user: "New project" or "Existing project"?
3. Based on answer, use the appropriate starter kit:
   - New project → Follow `CE-Starter-Kit-for-New-Project/KICKSTART.md` process
   - Existing project → Follow `CE-Starter-Kit-for-Optimize/KICKSTART.md` process
4. Generate only the missing files (never overwrite existing ones)
5. Run `scan` again to confirm everything is set up

### `validate [path]` — Validate context files quality
Check context files for quality issues and provide actionable feedback.

Validation rules:
1. **CLAUDE.md**:
   - Must contain project-specific rules (not generic/placeholder)
   - Should be under 80 lines (concise)
   - Must include testing requirements
   - Must include code style conventions

2. **PLANNING.md**:
   - Must contain architecture description
   - Must contain tech stack information
   - Should be under 120 lines
   - Must reference actual file paths, not placeholders

3. **TASK.md**:
   - Must have Active Tasks section
   - Must have Completed Tasks section
   - Tasks should have dates

4. **INITIAL.md**:
   - Must have FEATURE section
   - Must have EXAMPLES section
   - Must have DOCUMENTATION section
   - Should not contain only placeholder text

Output format per file:
```
Validating: CLAUDE.md
  ✅ Contains project-specific rules
  ⚠️  Warning: 95 lines (recommended: under 80)
  ✅ Testing requirements present
  ❌ Missing: code style conventions
  Score: 3/4
```

### `update <file> [path]` — Update a specific context file
Interactively update a context engineering file. Read the current file, analyze the codebase for changes, and suggest updates.

Steps:
1. Read the specified file (CLAUDE.md, PLANNING.md, TASK.md, or INITIAL.md)
2. Scan the codebase for changes since the file was last updated
3. Suggest specific updates based on:
   - New files/modules added
   - New dependencies installed
   - New patterns detected
   - Completed tasks (for TASK.md)
4. Present changes to user for approval before applying

### `diff [path1] [path2]` — Compare context files between two workspaces
Compare context engineering setups between two directories and highlight differences.

Steps:
1. Run `scan` on both paths
2. For each shared file, show a summary of differences:
   - Sections present in one but not the other
   - Different conventions or rules
   - Different tech stacks
3. Suggest what could be borrowed from one workspace to improve the other

### `export [path] [output]` — Export context files as a portable bundle
Package all context engineering files into a single markdown bundle for sharing or backup.

Steps:
1. Collect all context files from the workspace
2. Bundle them into a single markdown file with clear separators
3. Include metadata (date, file count, workspace path)
4. Save to the specified output path (default: `context-bundle-YYYY-MM-DD.md`)

### `status` — Quick status overview across multiple repos
Show a quick summary of context engineering status for all git repos found in subdirectories.

Steps:
1. Find all directories containing `.git/`
2. Run a lightweight scan on each
3. Display a compact summary table:
```
Workspace Context Engineering Status
─────────────────────────────────────────────
  repo-a/     ████████░░ 5/7  Missing: TASK.md, examples/
  repo-b/     ██████████ 7/7  Complete
  repo-c/     ██░░░░░░░░ 1/7  Missing: most files
─────────────────────────────────────────────
```

---

## Execution

Based on the action parsed from `$ARGUMENTS`, execute the corresponding steps above. If no action is provided or the action is not recognized, display the list of available actions with brief descriptions.

If the path argument is not provided, use the current working directory.

Always be thorough in scanning and validation. Use the Python tools in `src/context_engineer/` when available for consistent file analysis.
