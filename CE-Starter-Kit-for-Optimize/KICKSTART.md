# KICKSTART — Context Engineering for Existing Project

> Copy this entire folder into your existing project root, then tell AI: **"Read KICKSTART.md and follow it."**

---

## Mode: Optimize (Existing Project)

You are setting up Context Engineering for an **existing project** that already has code, structure, and conventions.
Your job is to **scan the codebase, understand everything, and generate context files** that accurately reflect the project as it is — so that every future AI conversation produces code that fits perfectly into the existing codebase.

---

## Phase 1: Deep Scan the Codebase

Perform a thorough analysis of the project. Do NOT ask the user questions yet — discover as much as possible first.

### 1.1 Project Structure
- Run `tree` (or equivalent) to map the full directory structure
- Identify the root layout: monorepo? single app? library?
- Note the folder naming convention (kebab-case, camelCase, snake_case, PascalCase)

### 1.2 Tech Stack Detection
Scan these files to identify the stack:
- `package.json`, `requirements.txt`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `Gemfile`, `composer.json`, `pom.xml`, `build.gradle`
- `tsconfig.json`, `next.config.*`, `vite.config.*`, `webpack.config.*`
- `Dockerfile`, `docker-compose.yml`, `.github/workflows/`
- `.env`, `.env.example`, `.env.local`

Record:
- Primary language(s) and version
- Framework(s) and version
- Database (check ORM config, migrations, docker-compose)
- Package manager (lock file: package-lock.json, yarn.lock, pnpm-lock.yaml, uv.lock, poetry.lock)
- Test framework (check test config files and test directories)
- Linter/formatter (check config files: .eslintrc, .prettierrc, ruff.toml, pyproject.toml, .editorconfig)

### 1.3 Code Patterns Analysis
Read 3-5 representative source files and identify:
- **Import style**: relative vs absolute, path aliases
- **Naming conventions**: variables, functions, classes, files
- **Error handling pattern**: custom exceptions? try-catch style? Result types?
- **Module organization**: how are features separated?
- **State management**: (if frontend) what library/pattern?
- **API patterns**: (if backend) REST conventions, middleware, auth

### 1.4 Testing Patterns
- Find existing test files
- Identify test framework and runner
- Note test file naming convention (test_*.py, *.test.ts, *_test.go)
- Note mocking/stubbing patterns used
- Note fixture or setup patterns

### 1.5 Documentation Audit
- Check for existing README.md (and its quality)
- Check for inline comments style
- Check for docstrings / JSDoc / GoDoc patterns
- Check for any existing architecture docs

### 1.6 Environment & Config
- List all environment variables from .env.example or .env
- Identify configuration pattern (env vars, config files, feature flags)
- Note any secrets management approach

---

## Phase 2: Confirm Findings with User

Present your findings as a structured summary and ask the user to confirm or correct:

```
I've analyzed your project. Here's what I found:

Project: [detected name]
Language: [detected] v[version]
Framework: [detected] v[version]
Database: [detected]
Test Framework: [detected]
Linter/Formatter: [detected]
Architecture: [detected pattern]

Key patterns I noticed:
- [pattern 1]
- [pattern 2]
- [pattern 3]

Is this correct? Anything I missed or got wrong?
Also, are there any specific rules or preferences you want to add
that aren't visible in the code?
```

Wait for the user's response before proceeding.

---

## Phase 3: Generate Context Files

After confirmation, generate the following files **in the project root**. Use the templates in `templates/` as the base and fill them with your findings.

### Files to Generate

| File | Source Template | Purpose |
|------|----------------|---------|
| `CLAUDE.md` | `templates/CLAUDE.md.template` | Global AI rules based on detected patterns |
| `PLANNING.md` | `templates/PLANNING.md.template` | Architecture documentation based on actual code |
| `TASK.md` | `templates/TASK.md.template` | Task tracking (start fresh) |
| `INITIAL.md` | `templates/INITIAL.md.template` | Feature request template |

### Generation Rules
1. **Base everything on actual code** — don't invent conventions that aren't in the codebase
2. **Replace all `[PLACEHOLDER]` values** with real information from your scan
3. **Remove sections that don't apply** to this project
4. **Include actual file paths** — reference real files as examples (e.g., "follow the pattern in `src/services/userService.ts`")
5. **Capture existing test patterns** — reference actual test files as examples
6. **Be specific about the stack** — don't write generic rules, write rules for THIS project
7. **Include detected gotchas** — if you noticed inconsistencies or anti-patterns, note them in CLAUDE.md so AI avoids repeating them

---

## Phase 4: Identify Improvement Opportunities (Optional)

After generating context files, briefly note any improvements the user might want to consider. Present these as suggestions, not actions:

```
Optional improvements I noticed:
- [ ] [e.g., "No .env.example exists — consider creating one"]
- [ ] [e.g., "Tests exist but no CI/CD pipeline detected"]
- [ ] [e.g., "No consistent error handling pattern — might want to standardize"]
- [ ] [e.g., "Some files exceed 500 lines — consider refactoring"]
```

Do NOT implement these. Just list them. The user decides what to act on.

---

## Phase 5: Cleanup

After all files are generated and the user confirms they look good:

1. **Delete** the `templates/` folder (no longer needed)
2. **Delete** this `KICKSTART.md` file (its job is done)
3. **Confirm** with the user that everything is set up

---

## Phase 6: Summary

Print a summary for the user:

```
Context Engineering Setup Complete!

Created files:
  - CLAUDE.md        → AI rules based on your existing code patterns
  - PLANNING.md      → Architecture documentation from codebase analysis
  - TASK.md          → Task tracking (ready to use)
  - INITIAL.md       → Template for feature requests

Detected and documented:
  - [X] Tech stack and versions
  - [X] Code patterns and conventions
  - [X] Testing patterns
  - [X] Project structure
  - [X] Environment configuration

Next steps:
  1. Review each generated file and adjust as needed
  2. When you want to add a feature, edit INITIAL.md with your requirements
  3. Use /generate-prp INITIAL.md to create a detailed implementation blueprint
  4. Use /execute-prp PRPs/feature-name.md to implement the feature
```

---

## Important Reminders

- **Scan first, ask second.** Discover as much as possible from the code before asking the user.
- **Document what IS, not what should be.** If the codebase uses tabs, document tabs — don't switch to spaces.
- **Be specific.** Reference actual file paths, actual function names, actual patterns.
- **Don't refactor.** Your job is to document the project, not to change it.
- **Keep files concise.** CLAUDE.md under 80 lines. PLANNING.md under 120 lines. Quality over quantity.
