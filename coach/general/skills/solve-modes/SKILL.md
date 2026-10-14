---
name: solve-modes
description: Every Formula Student quiz problem, live or practice, is solved twice - first a quick answer from one agent, logged at once, then a team of sub-agents that solves independently, compares its result with every answer the other members logged for the same question, and logs which answer is right and why, again each time a new answer arrives. Use at the start of every problem.
---

# Quick answer, then team answer

Made for the live quiz: several members solve the same questions at the same time, each with their own agent, and nobody knows the right answer yet. The log is where their agents meet. Every question gets both answers: the quick one so the team has something to submit in time, the team one to make sure it is right.

## 0. Join the live quiz
At the start, one member opens a live session: `start_session(competition, year, live: true)` returns a code. The others join with `join_session(code)`. Every entry for a question carries the session and the question's number in the quiz, so all members' answers to it line up.

## 1. Quick answer
1. The member gives the question number, the text and any images. Read the answers already logged for it (`get_answers(session, question)`) and the lessons for its topic (`get_lessons`). Check it against `COMPETITION.md`: if it is of a kind that file does not cover, follow its "When something is new".
2. One agent solves once by `solving-rules`: givens with units, SI, Python, plausibility, format.
3. Give the member the answer at once, marked **Quick answer**, with confidence.
4. Log it right away with `mode: quick` (`log-use`), so the other members see it.

Then start the team. Don't wait for the member.

## 2. Team answer
5. Start 2 or 3 sub-agents (`dispatching-parallel-agents`). Give each one the question, the competition folder, the relevant rules and `solving-rules`. Don't give them the quick answer, the logged answers or each other's work. Ask one of them to use a different method when one exists (e.g. energy instead of forces).
6. Each sub-agent returns: final answer, method, the script it ran, rule references, confidence.
7. Compare the sub-agents. They agree when their answers are equal after rounding to the required format. When they differ, find the first step where they split (a rule read differently, a unit, radius vs diameter, an assumption). Send that step back to the ones that differ, with the other side's reasoning for that step only, and ask them to re-check it. At most 2 rounds.

## 3. Compare with the other members
8. Read `get_answers(session, question)` again: the quick and team answers the other members logged meanwhile, with their feedback.
9. For each answer that differs from yours, find the first step where the two split. If its argument shows a step your team missed, send that step to the sub-agents to re-check before deciding.
10. Give the member the result, marked **Team answer**, with how many independent solutions match it, yours and the other members'. If it differs from your quick answer, say that first: the quick answer was wrong, this is the right one, and why.
11. Log it with `mode: team`. In `feedback` put the argument for your answer and, for every other answer logged for this question, whether it is right and why (e.g. "12.5 kN from another member wrong: took the diameter as the radius").

## 4. And so on, until the answers agree
12. While the question is open, keep checking `get_answers`: in a terminal agent every 30 seconds, in a web chat when the member writes `check`.
13. When a new answer or new feedback disagrees with yours, re-check the disputed step (with the sub-agents when you have them). Log the outcome with `mode: review`: your answer, kept or changed, and why. If you were wrong, say so to the member at once.
14. Stop when the latest answers of every member agree, or the time for the question is up.

## What to submit
- Tell the member, marked **Submit**, the answer the latest entries agree on.
- When they don't agree: the answer with the most independent matching solutions whose argument nobody refuted. Show the other one, why it was rejected, and mark confidence low.
- If the quiz needs an answer before the team is done, the member submits the quick answer. The team answer and the reviews still finish and are logged.

## Practice on past problems
The same steps, in a practice session (`start_session(competition, year)`), alone or with other members. `problem.md` holds the FS Quiz answer: don't use it while solving. Compare with it only after your team answer is logged, to fill `result`.

## Agents without sub-agents
Web chats (Claude Project, ChatGPT, Gemini) do the same steps one after another in the same conversation:
- quick answer and its log entry
- two more solutions from scratch, each with a different method and without looking at the earlier ones
- then steps 8 to 14

## Without the live log
Until a member's agent can reach the log (no MCP), the member pastes the other members' entries from the team chat and writes `check`; the agent prints its own entries for the member to share there (`log-use`).

## After the quiz
When the official answers are out, a topic checker marks each entry `correct` or `wrong`, so the lessons from the live quiz count for the next one.
