# A4. Log service

The log lives in the quiz workflow app's PostgreSQL database, not in git. Agents read and write it live through an MCP server or a REST API. Built in this repo as the first slice of the app.

## A4.0 Hosting — **Decision**
Moved here from 1.6: the log must be online for the trial.
Requirements: PostgreSQL, HTTPS, env secrets, long-lived connections (MCP over HTTP, notifications later).
Candidates: Railway; Vercel + Neon; own server with Docker.

## A4.1 App skeleton and database
Same as app tasks 1.1, 1.2 and 1.4 (skeleton, database, CI). Done here first.

## A4.2 Log table and REST API
Branch: `feat/log-api`. After A4.1.
- Table `log_entry`: id, user_id, competition, problem_id, topic, agent, result, approach, what_went_wrong, why, rule_for_next_time, status (`unreviewed` | `confirmed` | `rejected`), reviewed_by, created_at
- `GET /api/log?competition=&problem=&topic=&status=` (newest first, paged); `POST /api/log` validates the fields
- Auth: personal API token per member (`Authorization: Bearer`), stored hashed
Done when: unit tests on validation; integration test writes and reads an entry with a token.

## A4.3 MCP server
Branch: `feat/log-mcp`. After A4.2. Skill `mcp-builder`.
- Remote MCP endpoint (`/api/mcp`, streamable HTTP) on the same app, same token
- Tools: `get_lessons(competition, problem_id?, topic?)`, `add_log_entry(...)`; entries marked `unreviewed` are labelled as such in results
Done when: Claude Code and one web agent connect, read and write an entry.

## A4.4 API tokens
Branch: `feat/api-tokens`. After A4.2.
- Member requests a token; admin approves or rejects; member sees the token once and can revoke it
- Until accounts exist (app step 2), a seed script creates tokens for the trial members
Done when: a revoked token gets 401.

## A4.5 Paste form
Branch: `feat/log-paste-form`. After A4.2.
- Page where a member pastes the entry an agent without MCP printed; same validation as the API
Done when: a pasted entry appears in `GET /api/log`.

## A4.6 Log review
Branch: `feat/log-review`. After A4.2.
- Admin and topic checkers list unreviewed entries and mark them confirmed or rejected
- A lesson that repeats is moved into a skill in the coach repo by a maintainer
Done when: e2e: an entry goes from unreviewed to confirmed.
