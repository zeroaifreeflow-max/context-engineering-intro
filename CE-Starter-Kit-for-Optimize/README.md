# CE Starter Kit — Optimize Existing Project

Context Engineering Starter Kit for adding AI-ready context to **existing projects** that already have code.

## What is this?

This kit analyzes your existing codebase and generates **Context Engineering** files that capture your project's patterns, conventions, and architecture — so that AI coding assistants produce code that fits perfectly into your codebase from the first pass.

The AI scans your code first, then generates context files based on what it actually finds. No generic templates — everything is specific to YOUR project.

## How to Use

### Step 1: Copy this folder into your existing project root
```bash
cp -r CE-Starter-Kit-for-Optimize/ /path/to/your/existing/project/
```

### Step 2: Open the project in your AI-powered editor and tell AI:
```
Read KICKSTART.md and follow it.
```

### Step 3: Let AI scan your codebase
The AI will automatically analyze your:
- Tech stack and versions
- Code patterns and conventions
- Testing patterns
- Project structure
- Environment configuration

### Step 4: Confirm the findings
The AI will present a summary of what it detected. Confirm or correct anything it got wrong.

### Step 5: Review the generated files
The AI will create:
- `CLAUDE.md` — Rules based on your actual code patterns
- `PLANNING.md` — Architecture docs from codebase analysis
- `TASK.md` — Task tracker
- `INITIAL.md` — Template for requesting new features

### Step 6: Start building with context
Use the PRP workflow for new features:
```
1. Edit INITIAL.md with your feature requirements
2. /generate-prp INITIAL.md
3. /execute-prp PRPs/feature-name.md
```

## What's Inside

```
CE-Starter-Kit-for-Optimize/
├── KICKSTART.md                      # Main instruction file for AI
├── README.md                         # This file
└── templates/
    ├── CLAUDE.md.template            # Template for AI rules
    ├── PLANNING.md.template          # Template for architecture docs
    ├── TASK.md.template              # Template for task tracking
    └── INITIAL.md.template           # Template for feature requests
```

## How is this different from the New Project kit?

| | New Project Kit | Optimize Kit (this one) |
|---|---|---|
| **Starting point** | No code yet | Existing codebase |
| **How it works** | Interviews you, then creates files | Scans your code, then creates files |
| **CLAUDE.md content** | Based on your preferences | Based on your actual patterns |
| **PLANNING.md content** | Based on your design choices | Based on detected architecture |

## Key Principle

> Most AI failures aren't model failures — they're **context failures**.
> Your codebase already has patterns. This kit makes sure AI knows them.
