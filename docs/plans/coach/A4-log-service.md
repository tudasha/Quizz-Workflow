# A4. Log service

The log and every solve live in the quiz workflow app's PostgreSQL database, not in git. Agents read and write them live through an MCP server or a REST API. Built in this repo as the first slice of the app. Every member sees the log and the dashboard; only admins review entries and approve tokens.

## A4.0 Hosting — **Decision**
Moved here from 1.6: the log must be online for the trial.
Requirements: PostgreSQL, HTTPS, env secrets, long-lived connections (MCP over HTTP, notifications later).
Candidates: Railway; Vercel + Neon; own server with Docker.

## A4.1 App skeleton and database
Same as app tasks 1.1, 1.2 and 1.4 (skeleton, database, CI). Done here first.

## A4.2 Log table and REST API
Branch: `feat/log-api`. After A4.1.
- Table `log_entry`: id, user_id, session_id, question (number in the quiz), competition, problem_id, question_text, topic, agent, mode (`quick` | `team` | `review`), answer, result, approach, what_went_wrong, why, rule_for_next_time, feedback, status (`unreviewed` | `confirmed` | `rejected`), reviewed_by, created_at
- `GET /api/log?competition=&problem=&topic=&status=&session=&question=` (newest first, paged); `POST /api/log` validates the fields
- Auth: personal API token per member (`Authorization: Bearer`), stored hashed
Done when: unit tests on validation; integration test writes and reads an entry with a token.

## A4.3 MCP server
Branch: `feat/log-mcp`. After A4.2. Skill `mcp-builder`.
- Remote MCP endpoint (`/api/mcp`, streamable HTTP) on the same app, same token
- Tools: `start_session(competition, year, live?)` (returns a code), `join_session(code)`, `get_answers(session, question)` (every member's answers, reviews and feedback for that question, newest first, so the agents of a live quiz can compare), `get_lessons(competition, topic?, problem_id?)`, `add_log_entry(...)`, `record_answer(session, question, answer, time_s)`; entries marked `unreviewed` are labelled as such in results
Done when: two agents (Claude Code and one web agent) join the same live session, each logs an answer to question 1 and each sees the other's with `get_answers`.

## A4.7 Solve sessions
Branch: `feat/solve-sessions`. After A4.2.
- Table `solve_session`: id, code, live (true for a real quiz), created_by, competition, year, started_at; filed automatically by competition and year
- Table `session_member`: session_id, user_id, agent, joined_at
- Table `solve_answer`: session_id, user_id, question, problem_id, answer, correct (true / false / unknown; unknown until the official answers are out), time_s, log_entry_id
- REST endpoints mirror the MCP tools; the paste form also accepts a session summary
Done when: integration test records a session with three answers and links a log entry.

## A4.8 Dashboard
Branch: `feat/coach-dashboard`. After A4.7.
- Visible to every member: scores per competition, year, topic and agent; weak topics; latest sessions; unreviewed log entries count
- Live view of a session: for each question, every member's latest answer and whether they agree, so the member who submits sees it at a glance
Done when: e2e shows the scores of a seeded session.

## A4.9 Search tools for agents
Branch: `feat/mcp-search`. After A4.3.
- The zip build Action (A5.1) also uploads a search index of its content (rules and handbook sections, problems, solutions)
- MCP tools: `search_rules(query or rule number)`, `search_problems(query, topic?, competition?)`, `get_problem(id)` (problem, solution.py, solution.md)
- Same tools for every agent with MCP, not only Claude Code
Done when: `search_rules("T 11.2")` returns that rule's text; `search_problems` finds a problem by a phrase from it.

## A4.4 API tokens
Branch: `feat/api-tokens`. After A4.2.
- Member requests a token from their account; admin approves or rejects; member sees the token once and can revoke it
- Until accounts exist (app step 2), a seed script creates tokens for the trial members
Done when: a revoked token gets 401.

## A4.5 Paste form
Branch: `feat/log-paste-form`. After A4.2.
- Page where a member pastes the entry an agent without MCP printed; same validation as the API
Done when: a pasted entry appears in `GET /api/log`.

## A4.6 Log review
Branch: `feat/log-review`. After A4.2.
- Admin and topic checkers list unreviewed entries and mark them confirmed or rejected
- A lesson that repeats is moved into a skill in `coach/` by a maintainer
Done when: e2e: an entry goes from unreviewed to confirmed.
