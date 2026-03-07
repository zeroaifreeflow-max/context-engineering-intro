# PLANNING.md — Context Engineering Intro

## Project Overview
A comprehensive template for Context Engineering — providing AI coding assistants with the structured context they need to produce production-ready code.

## Architecture
```
context-engineering-intro/
├── .claude/commands/           # Claude Code slash commands (skills)
├── CE-Starter-Kit-for-New-Project/  # Bootstrap kit for new projects
├── CE-Starter-Kit-for-Optimize/     # Optimization kit for existing projects
├── PRPs/                       # Product Requirements Prompts
├── examples/                   # Code examples for AI reference
├── src/context_engineer/       # Python tools for context file management
├── tests/                      # Unit tests
├── use-cases/                  # Real-world use case examples
├── validation/                 # Validation templates
├── CLAUDE.md                   # Global AI rules
├── PLANNING.md                 # This file
├── TASK.md                     # Task tracking
└── INITIAL.md                  # Feature request template
```

## Tech Stack
- **Language**: Python 3.x
- **Testing**: pytest
- **Linter/Formatter**: black, ruff
- **Data Validation**: pydantic
- **Virtual Environment**: venv_linux

## Key Patterns
- Slash commands in `.claude/commands/*.md` for Claude Code integration
- Template-based file generation (CE Starter Kits)
- PRP workflow: INITIAL.md → /generate-prp → PRP → /execute-prp → Implementation

## Conventions
- Follow PEP8, use type hints
- Google-style docstrings
- Files under 500 lines
- Module organization: agent.py, tools.py, prompts.py
