# Project context

Snapshot of decisions from the claude.ai project "Formula Student AI learning" (updated 2026-10-14). Owner: Gion.
If something here conflicts with a newer instruction from Gion, the instruction wins.

## Goal
Help the team train for Formula Student quizzes (math, physics, mechanics, electronics, rulebook, marketing) using past quizzes and verified solutions.

## Two parts
1. **Quiz workflow app** (this repo): quizzes, problem assignment, answers, documentation, AI coach panel.
2. **AI coach knowledge repo** (separate repo, not created yet): shared rules, skills and past problems that each member loads into their own agent. No model training, no in-app chat.

## Quiz workflow app

### Decisions
- Stack (Gion, 2026-10-14): Next.js + TypeScript, PostgreSQL + Drizzle, Better Auth, Tailwind + shadcn/ui, Vitest + Playwright, Cloudflare R2 for files, GitHub API for the coach repo. No Firebase or Firestore.
- Hosting: still open (candidates: Railway, Vercel + Neon, own server).
- App repo: https://github.com/tudasha/Quizz-Workflow (Gion's account; the ARTTU-Software/Quiz-Workflow repo held the firmware template)
- Admin rights from a server-side role; admin passkey checked on the server.
- Departments: Accumulator, Electrical, Mechanical, Dynamics, Marketing.
- No AI chat for now.

### Pages
- Login: username and password, department on first login, admin passkey
- Home: list of quizzes; admins create and save quizzes
- Quiz page: problem gallery and problem detail
- Documentation: collections per department or for the whole team
- AI coach panel: competition selector, setup prompt, zip download, log entry form
- Admin only: Departments, Assignments, All Answers

### Build steps
1. Setup: choose stack, create repo with branch protection and CI, design DB (users, departments, quizzes, problems, assignments, answers, documentation)
2. Accounts: sign up / log in, auto-login through a proper auth service, department on first login, server-side admin role and passkey, logout, username badge
3. Quizzes and problems:
   - Gallery cards by number, status badge (Available, N Assigned, Completed), final answer once completed
   - Highlights: red = assigned to me, gold = my department, green = completed and relevant to me
   - Hover preview of the problem image
   - Admin: add, edit title, delete problem, image upload
   - Detail: assign to me, assign to another (username checked), unassign
   - One answer per user per problem; resubmit updates it
   - Mark as Completed (with final answer), Mark as Available (admin)
   - AI check of answered problems with a confidence tag
4. Admin views: Departments (assign, relocate, delete users), Assignments (per user with date and time), All Answers (grouped by problem, similarity highlighting)
5. Notifications: action toasts 3 s; queued "assigned to you" notifications 5 s each; connection status indicator
6. Documentation page: PDFs, .md files, images; title, description, creator
7. AI coach panel: competition selector, setup prompt with Copy button, zip download of `general/` + chosen competition, log entry form that saves to the coach repo `log` branch, request push access to the `log` branch (admin approves)
8. Usage tutorial (last)

### Open points
- Hosting
- How answer similarity is measured (exact, numeric tolerance or AI)
- Which AI model does the answer check
- Where the AI coach repo is hosted

## AI coach knowledge repo (for reference)

```
AGENTS.md            shared prompt: order of work, folders to read, when to log
CLAUDE.md            points to AGENTS.md
general/
  skills/            solving rules (decimals, units, answer format), log entry
  rules/             FS Rules, by version
  tools/             formula library, checks
competitions/
  fsa/ fs-alpe-adria/ fsg/ ...
    COMPETITION.md   quiz format, decimals, time limit, scoring
    skills/          competition-specific calculation rules
    handbook/        by year
    problems/<id>/   problem.md, solution.py, solution.md
log/                 one file per solve (on the log branch)
```

- Agents with git (Claude Code, Codex) get a setup prompt: clone or pull, read AGENTS.md, use `general/` + one competition, pull before each problem, push a log entry after.
- Agents without git (Claude Project, ChatGPT, Gemini) get a zip; the agent writes the log entry as text and the member pastes it into the app's log form.
- Log entry: correct or not, approach, what went wrong, why, rule for next time.
- `main` protected with PRs; agents push only to the `log` branch. Entries are unreviewed until a topic checker confirms them; skills win over log entries.
- About 100 verified problems are kept as a test set outside the repo.
- Problems imported from the FS Quiz site only with the owner's permission.
- CI: pytest plus running every `solution.py`.

## Later
- Agents argue with each other until they agree
- AI chat in the app
