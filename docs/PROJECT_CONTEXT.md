# Project context

Snapshot of decisions from the claude.ai project "Formula Student AI learning" (updated 2026-10-14). Owner: Gion.
If something here conflicts with a newer instruction from Gion, the instruction wins.

## Goal
Help the team train for Formula Student quizzes (math, physics, mechanics, electronics, rulebook, marketing) using past quizzes and verified solutions.

## Two parts
Order (Gion, 2026-10-14): the AI coach is built and reviewed first, then the quiz workflow app. Plan: `docs/plans/README.md`.

1. **Quiz workflow app** (this repo): quizzes, problem assignment, answers, documentation, AI coach panel.
2. **AI coach**: content in `coach/` in this repo (maintainers edit it by PR) with shared rules, skills and past problems, handed to members as one zip; plus a live log in this app's database that every agent reads and writes through MCP or a REST API. No model training, no in-app chat.

## Quiz workflow app

### Decisions
- Stack (Gion, 2026-10-14): Next.js + TypeScript, PostgreSQL + Drizzle, Better Auth, Tailwind + shadcn/ui, Vitest + Playwright, Cloudflare R2 for files. No Firebase or Firestore.
- Hosting: still open (candidates: Railway, Vercel + Neon, own server); needed before the coach trial (A4.0).
- App repo: https://github.com/tudasha/Quizz-Workflow (Gion's account; the ARTTU-Software/Quiz-Workflow repo held the firmware template)
- Admin rights from a server-side role; admin passkey checked on the server.
- Departments: Accumulator, Electrical, Mechanical, Dynamics, Marketing.
- No AI chat for now.

### Pages
- Login: username and password, department on first login, admin passkey
- Home: list of quizzes; admins create and save quizzes
- Quiz page: problem gallery and problem detail
- Documentation: collections per department or for the whole team
- AI coach panel: one zip download, copy prompt per competition, MCP URL and token, paste form, log browser, dashboard
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
7. AI coach panel: competition selector, one zip download, copy prompt per competition, MCP URL and API token request (admin approves), paste form, log browser, dashboard
8. Usage tutorial (last)

### Open points
- Hosting
- How answer similarity is measured (exact, numeric tolerance or AI)
- Which AI model does the answer check

## AI coach (Part A, built first)

Data source: FS Quiz API v2 `https://api.fs-quiz.eu/2/` (events, quizzes, questions with answers and `is_correct`, solutions, images, rulebooks and handbooks). Licence ODbL: credit FS Quiz; a shared derived database stays ODbL.

```
coach/
  AGENTS.md            shared prompt
  CLAUDE.md            points to AGENTS.md
  SOURCES.md           FS Quiz credit, ODbL
  general/
    skills/            solving rules, log use
    rules/             FS Rules: current/ (2026) for agents, older years for reference
    tools/             FS Quiz import script, checks
    scripts/           shared calculation scripts (filled after the trial)
  competitions/
    fsa/ fs-alpe-adria/ fsg/ ...
      COMPETITION.md   quiz format, decimals, time limit, scoring
      skills/          competition-specific calculation rules
      handbook/        current/ (2026) for agents, older years for reference
      problems/<id>/   problem.md, solution.py, solution.md
```

- Members never need git (not everyone has access). They download one zip with every competition in its own folder (`AGENTS.md` + `LOG.md` + `general/` + `competitions/*`) and copy a short prompt from the app naming their competition. The zip holds only the current-year rules and handbook, and agents rely on them.
- The log is in this app's PostgreSQL. Agents read lessons before each problem and write an entry after it, live, through the MCP server or REST API with a personal token; agents without MCP print the entry and the member pastes it into the app.
- Every solve is stored in a session (member, agent, competition, year; answer, correct or not, time) and shown on a dashboard everyone can see.
- The MCP server also offers search over rules, handbooks and past problems.
- Made for the live quiz, where nobody knows the answers yet: members join one live session; every question gets a quick answer (one agent, logged at once) and then a team answer (sub-agents that compare with the other members' logged answers and log which is right and why, re-checking until they agree), described in `coach/general/skills/solve-modes/`.
- Log entry: problem, agent, correct or not, approach, what went wrong, why, rule for next time. Entries are `unreviewed` until a topic checker confirms them; skills win over log entries.
- Claude wrote `AGENTS.md` and the general skills; Gion reviews them. Per-competition rules (`COMPETITION.md`, competition skills) come from Gion's text.
- About 100 verified problems are kept as a test set outside the repo.
- Coach CI (only when `coach/` changes): pytest plus running every `solution.py`.

## Later
- Local fine-tuned model
