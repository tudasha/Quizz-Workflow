# AGENTS.md - FS Quiz Workflow app

Web app for the Formula Student team: admins build quizzes from problems, members get problems assigned and submit answers, and each member gets the AI coach repo for a competition.

Project context and decisions: @docs/PROJECT_CONTEXT.md
Build plan, one file per step: `docs/plans/` (start with `docs/plans/README.md`).
Coding guidelines: `docs/CODING_GUIDELINES.md`. Claude Code also loads the same rules from `.claude/rules/` and skills from `.claude/skills/`.

## Stack
- Next.js (App Router) + TypeScript, front end and back end in one project
- PostgreSQL + Drizzle ORM (schema in `src/server/db/schema.ts`, migrations in `drizzle/`)
- Better Auth: username and password, sessions, server-side roles
- Tailwind CSS + shadcn/ui
- Vitest (logic), Playwright (browser tests)
- Files (images, PDFs): Cloudflare R2 (S3 API)
- AI coach repo access: GitHub API (Octokit)
- Package manager: pnpm
- Hosting: not chosen yet. Do not pick one; ask. Code must not depend on a specific host.
- Never Firebase or Firestore.

## Layout
- `src/app/`: routes and pages
- `src/components/`: UI components
- `src/lib/`: pure logic, no database or network (unit tested)
- `src/server/`: database, auth, storage, GitHub and other services
- `drizzle/`: migrations
- `tests/e2e/`: Playwright tests

## Commands
- Install: `pnpm install`
- Local database: `docker compose up -d db`
- Migrations: `pnpm db:generate` then `pnpm db:migrate`
- Run locally: `pnpm dev`
- Unit tests: `pnpm test`
- Browser tests: `pnpm test:e2e`
- Lint and types: `pnpm lint` and `pnpm typecheck`

## Working rules
- If a requirement is ambiguous, stop and ask (skill `grilling`) before writing code.
- Keep changes small and atomic. Do not refactor unrelated files or change formatting.
- Keep command output short: `git status -s`, `git log -n 5 --oneline`, `git diff --stat`; run single test files while iterating.
- Never claim the build or tests pass without running them and reading the output.
- Run the full checks at milestones, not after every small edit.
- Never push to `main` or `dev`. Open a draft PR early with `gh pr create --draft --base dev --title "<task> <title>" --body-file <file>`.
- Never commit build output or secrets.
- Tasks marked **Decision** or **Gion** in `docs/plans/` wait for Gion. Part A (AI coach repo) comes before Part B (this app).

## Before every PR
1. Branch is `feat/`, `fix/`, `refactor/`, `test/` or `docs/`, based on `dev`.
2. `pnpm lint`, `pnpm typecheck`, `pnpm test` and `pnpm test:e2e` pass.
3. PR targets `dev`, uses the PR template, and names the plan task it covers (e.g. `3.4`).
