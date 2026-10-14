# 1. Setup

## 1.1 Project skeleton
Done in A4.1.
Branch: `feat/skeleton`
- Next.js (App Router) + TypeScript (strict), pnpm, Tailwind, shadcn/ui
- ESLint + Prettier (4 spaces), `pnpm lint`, `pnpm typecheck`
- Folders from CLAUDE.md "Layout"
- `.gitignore` (node_modules, .next, .env, coverage, playwright reports), `.env.example`
Done when: `pnpm dev` shows an empty home page; lint and typecheck pass.

## 1.2 Database and migrations
Done in A4.1.
Branch: `feat/database`. After 1.1.
- `docker-compose.yml` with PostgreSQL for local work
- Drizzle + drizzle-kit, `pnpm db:generate`, `pnpm db:migrate`
- `DATABASE_URL` from env
Done when: a fresh clone runs `docker compose up -d db && pnpm db:migrate` without errors.

## 1.3 Schema
Branch: `feat/schema`. After 1.2. Skill `domain-modeling` for names.
Tables (Better Auth adds its own user, session and account tables; extend its user):
- `user`: + `username` (unique), `role` (`member` | `admin`), `department_id` (nullable until first login)
- `department`: id, name (seed: Accumulator, Electrical, Mechanical, Dynamics, Marketing)
- `quiz`: id, title, competition (nullable), created_by, created_at
- `problem`: id, quiz_id, number, title, image_key, status (`available` | `completed`), final_answer, completed_by, completed_at
- `assignment`: problem_id, user_id, assigned_by, assigned_at; unique (problem_id, user_id)
- `answer`: problem_id, user_id, value, ai_confidence (nullable), created_at, updated_at; unique (problem_id, user_id)
- `doc_collection`: id, title, department_id (null = whole team), created_by
- `document`: id, collection_id, title, description, file_key, file_type, created_by, created_at
- `notification`: id, user_id, type, payload (json), created_at, read_at
- `log_entry` and `api_token`: added in A4
Done when: migration applies; a seed script creates departments and the first admin account from env.

## 1.4 CI
Done in A4.1.
Branch: `feat/ci`. After 1.1.
- GitHub Actions on PRs into `dev` and `main`: install, lint, typecheck, unit tests, e2e tests against a Postgres service
Done when: a PR shows all checks green.

## 1.5 Branch protection
Not code; Gion or a lead does it on GitHub.
- Create `dev`; protect `main` and `dev`: PR required, 1 approval, CI must pass

## 1.6 Hosting
Decided in A4.0.
