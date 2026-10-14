---
name: log-use
description: How to use the team's shared solve log - read lessons before a problem, write one entry after it, and record answers in a solve session. Use before and after every quiz problem.
---

# Using the shared log

The log lives in the team's quiz workflow app. Every member's agent reads and writes it live, so a mistake one agent logs helps all the others. How to connect is in `LOG.md`.

## Before a problem
- Call `get_lessons(competition, problem_id, topic)`. Without a problem id (a new question), use the competition and topic.
- Read `confirmed` lessons first. `unreviewed` entries are hints only; skills, rules and verified problems win over them.
- Mention in your answer any lesson you used.

## After a problem
Write one entry for every problem, right or wrong, with `add_log_entry`:

| Field | What to write |
|---|---|
| competition | folder name, e.g. `fsg` |
| problem_id | FS Quiz question id, or `new` plus the question text |
| topic | rules, maths, physics, mechanics, electronics, marketing, business |
| agent | agent and model, e.g. `Claude Code, Sonnet 5.5` |
| result | `correct`, `wrong`, or `unknown` (no official answer yet) |
| approach | method in one or two sentences |
| what_went_wrong | the mistake, or `nothing` |
| why | the cause, not the symptom |
| rule_for_next_time | one rule another agent can follow, or `none` |

- `result` is `correct` or `wrong` only when compared with the official answer in `problem.md` or given by the member.
- A recurring trap with no single problem (e.g. "FSA gives diameters, not radii") is an entry with `problem_id: note`.
- Never write the member's API token, passwords or personal data in an entry.

## Quiz runs
- At the start of a quiz or practice set: `start_session(competition, year)`.
- After each question: `record_answer(session, problem_id, answer, correct, time_s)`, then the log entry.

## Without MCP
Print the entry in this block at the end of your answer; the member pastes it into the Log entry form in the app.

```yaml
competition:
problem_id:
topic:
agent:
result:
approach:
what_went_wrong:
why:
rule_for_next_time:
```
