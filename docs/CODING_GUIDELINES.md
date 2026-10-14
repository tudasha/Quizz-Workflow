# Coding Guidelines

Team coding guidelines, adapted from the ARTTU firmware guidelines for this web app. Claude Code loads the same rules from `.claude/rules/`.

## Git workflow

### Branches
| Type | Prefix | Use | Merges into |
|---|---|---|---|
| Integration | `dev` | Active development and integration | `main` (lead only) |
| Feature | `feat/` | New functionality, e.g. `feat/problem-gallery` | `dev` |
| Bugfix | `fix/` | Bug fix, e.g. `fix/assign-username-check` | `dev` |
| Refactor | `refactor/` | Cleanup, no behaviour change | `dev` |
| Testing | `test/` | Experiments or new tests | `dev` |
| Docs | `docs/` | Documentation only | `dev` |

- Never push to `main` or `dev` directly. Always a PR from a prefixed branch into `dev`.
- A lead merges `dev` into `main` once `dev` is stable and tested on the deployed test environment.
- `main` is production-ready only: always safe to deploy.

### Commits
- One logical change per commit ("Add username check on assign", not "Work on app").
- Commit messages in English, imperative mood.

### Pull requests
- Open a draft PR early; it tells the team who is working on which module.
- At least one approval from a lead before merge.
- CI must be green before merge.

### Releases
- Every deploy to production is tagged (`v1.0.2`) with a GitHub Release.

## Code style

- Indentation: 4 spaces, no tabs (unless the chosen language's formatter enforces otherwise; then the formatter wins).
- Naming: `camelCase` or `snake_case` for variables and functions, following the language's convention, consistent within a file. `ALL_CAPS` for constants.
- Descriptive names: `assigned_problem_count`, not `apc`.
- Comments explain why, not what. Assume the reader knows the language but not your logic.
- Keep framework, database and network code apart from logic. Logic must be testable without a running server or database.

## Testing and CI

- Every PR must pass CI (build, lint, tests) before merge.
- New logic comes with unit tests. Bug fixes come with a test that fails before the fix.
- Database changes go through migrations, never manual edits to a shared database.
- Never skip, disable or delete a test to get CI green.

## Repo hygiene

- Never commit build output or binaries (`dist/`, `build/`, `node_modules/`, `.venv/`, `*.zip`, compiled files). Release builds go in GitHub Releases.
- Never commit secrets: passwords, API keys, the admin passkey, database URLs. They live in environment variables; `.env` is in `.gitignore`, `.env.example` lists the names only.
- Shared code is reused through a package or submodule, never copied in.
- The AI coach content lives in `coach/` in this repo (Gion, 2026-10-14). It is shipped to members as a zip; app code never imports from it.

## Security

- Admin rights come from a server-side role. The admin passkey is checked on the server, never in the client.
- Every admin action (delete, relocate, mark available, approve API tokens, review log entries) checks the role on the server.
- Assigning a problem to another user checks that the username exists, on the server.
- Passwords are hashed with a standard library (bcrypt or argon2), never stored or logged in plain text.
- All SQL uses parameters, never string concatenation.
- API tokens are stored hashed, shown once, revocable; every API and MCP call checks the token on the server.

## Using AI tools (Claude Code included)

- AI-written code must build and pass the full test suite before a PR is opened.
- If you do not understand what the AI wrote, do not merge it.
- Claude Code: work on a prefixed branch, open draft PRs into `dev`, never push to `main` or `dev`.
- Claude Code: do not choose the stack, add a hosted service, or change the database schema without asking.
