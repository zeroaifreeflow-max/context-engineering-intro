# KICKSTART — Context Engineering for New Project

> Copy this entire folder into your new project root, then tell AI: **"Read KICKSTART.md and follow it."**

---

## Mode: Bootstrap (New Project)

You are setting up Context Engineering for a **brand new project** that has little or no existing code.
Your job is to **interview the user, design the foundation, and generate all context files** so that every future AI conversation has the information it needs to produce production-ready code on the first pass.

---

## Phase 1: Interview the User

Ask the user the following questions. Wait for answers before proceeding. Do not assume anything.

### 1.1 Project Overview
- What is this project? (1-2 sentence description)
- What problem does it solve and for whom?
- Is this a personal project, a startup MVP, a client project, or enterprise?

### 1.2 Tech Stack
- Primary language(s)? (e.g., Python, TypeScript, Go, Rust)
- Framework(s)? (e.g., FastAPI, Next.js, Django, Express, SvelteKit)
- Database? (e.g., PostgreSQL, MongoDB, SQLite, Supabase, none yet)
- ORM / data layer? (e.g., SQLAlchemy, Prisma, Drizzle, none)
- Package manager? (e.g., pip/uv, npm/pnpm/bun, cargo)
- Deployment target? (e.g., Vercel, AWS, Docker, Cloudflare Workers)

### 1.3 Architecture & Patterns
- Preferred architecture? (e.g., monolith, microservices, serverless, modular monolith)
- API style? (REST, GraphQL, tRPC, gRPC, none)
- Authentication method? (e.g., JWT, session, OAuth, none yet)
- State management? (if frontend: Redux, Zustand, Context, Pinia, etc.)

### 1.4 Code Style & Preferences
- Linter / formatter? (e.g., black + ruff, ESLint + Prettier, rustfmt)
- Testing framework? (e.g., pytest, vitest, jest, go test)
- Preferred docstring / comment style?
- Any strong opinions? (e.g., "always use type hints", "no classes, only functions", "prefer composition over inheritance")

### 1.5 Known Requirements
- Key features planned for v1?
- External APIs or services to integrate?
- Any reference projects or examples to follow?

---

## Phase 2: Generate Context Files

After the interview, generate the following files **in the project root**. Use the templates in `templates/` as the base and fill them in with the user's answers.

### Files to Generate

| File | Source Template | Purpose |
|------|----------------|---------|
| `CLAUDE.md` | `templates/CLAUDE.md.template` | Global AI rules and project conventions |
| `PLANNING.md` | `templates/PLANNING.md.template` | Architecture, goals, constraints |
| `TASK.md` | `templates/TASK.md.template` | Task tracking |
| `INITIAL.md` | `templates/INITIAL.md.template` | Feature request template |

### Generation Rules
1. **Read each template** in `templates/` carefully
2. **Replace all `[PLACEHOLDER]` values** with real information from the interview
3. **Remove sections that don't apply** (e.g., no database section if the project doesn't use one)
4. **Add project-specific sections** if the user mentioned something not covered by the template
5. **Write files to the project root**, not inside the templates folder
6. **Adapt language-specific conventions** — don't use Python examples for a TypeScript project

---

## Phase 3: Create Project Structure

Based on the interview, create the initial folder structure.

### Rules
- Create folders only — do NOT create placeholder files unless the user asks
- Follow the conventions of the chosen framework (e.g., Next.js uses `app/` or `pages/`, FastAPI uses `src/`)
- Always include a `tests/` directory
- Always include a `.env.example` file with placeholder variables
- Add `.gitignore` appropriate for the tech stack

### Example Output (Python + FastAPI)
```
project-root/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   ├── models/
│   ├── services/
│   └── config/
├── tests/
├── .env.example
├── .gitignore
├── CLAUDE.md          ← generated
├── PLANNING.md        ← generated
├── TASK.md            ← generated
└── INITIAL.md         ← generated
```

### Example Output (TypeScript + Next.js)
```
project-root/
├── src/
│   ├── app/
│   ├── components/
│   ├── lib/
│   └── types/
├── tests/
├── .env.example
├── .gitignore
├── CLAUDE.md          ← generated
├── PLANNING.md        ← generated
├── TASK.md            ← generated
└── INITIAL.md         ← generated
```

---

## Phase 4: Cleanup

After all files are generated and the user confirms they look good:

1. **Delete** the `templates/` folder (no longer needed)
2. **Delete** this `KICKSTART.md` file (its job is done)
3. **Confirm** with the user that everything is set up

---

## Phase 5: Summary

Print a summary for the user:

```
Context Engineering Setup Complete!

Created files:
  - CLAUDE.md        → AI rules and project conventions
  - PLANNING.md      → Architecture and design decisions
  - TASK.md          → Task tracking (ready to use)
  - INITIAL.md       → Template for feature requests
  - .env.example     → Environment variables template
  - .gitignore       → Git ignore rules

Next steps:
  1. Review each generated file and adjust as needed
  2. When you want to add a feature, edit INITIAL.md with your requirements
  3. Use /generate-prp INITIAL.md to create a detailed implementation blueprint
  4. Use /execute-prp PRPs/feature-name.md to implement the feature
```

---

## Important Reminders

- **Do NOT skip the interview.** The quality of context engineering depends on understanding the project.
- **Do NOT generate generic content.** Every line in CLAUDE.md and PLANNING.md should be specific to this project.
- **Do NOT use placeholder values.** If you don't know something, ask the user.
- **Keep files concise.** CLAUDE.md should be under 80 lines. PLANNING.md should be under 120 lines. More is not better — clarity is.
