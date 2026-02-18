# CE Starter Kit — New Project

Context Engineering Starter Kit for bootstrapping **brand new projects** with AI-ready context from day one.

## What is this?

This kit helps you set up **Context Engineering** — a system of structured files that give AI coding assistants all the information they need to produce production-ready code on the first pass.

Instead of repeating instructions every conversation, you create persistent context files (`CLAUDE.md`, `PLANNING.md`, `TASK.md`) that the AI reads automatically.

## How to Use

### Step 1: Copy this folder into your new project
```bash
cp -r CE-Starter-Kit-for-New-Project/ /path/to/your/new/project/
```

### Step 2: Open the project in your AI-powered editor and tell AI:
```
Read KICKSTART.md and follow it.
```

### Step 3: Answer the interview questions
The AI will ask you about your tech stack, architecture, and preferences. Answer honestly — this is the foundation for all future AI interactions in this project.

### Step 4: Review the generated files
The AI will create:
- `CLAUDE.md` — Rules the AI follows in every conversation
- `PLANNING.md` — Your project's architecture and design decisions
- `TASK.md` — Task tracker
- `INITIAL.md` — Template for requesting new features

### Step 5: Start building
Use the PRP workflow for new features:
```
1. Edit INITIAL.md with your feature requirements
2. /generate-prp INITIAL.md
3. /execute-prp PRPs/feature-name.md
```

## What's Inside

```
CE-Starter-Kit-for-New-Project/
├── KICKSTART.md                      # Main instruction file for AI
├── README.md                         # This file
└── templates/
    ├── CLAUDE.md.template            # Template for AI rules
    ├── PLANNING.md.template          # Template for architecture docs
    ├── TASK.md.template              # Template for task tracking
    └── INITIAL.md.template           # Template for feature requests
```

## Key Principle

> Most AI failures aren't model failures — they're **context failures**.
> Give AI the right context, and it delivers the right code.
