# A3. Rules and skills

Gion, 2026-10-14: Claude writes `AGENTS.md` and the general skills (A3.1, A3.2, A3.5), Gion reviews them. The per-competition rules (A3.4) come from Gion's text: agents format them, keep the wording and ask about gaps instead of filling them.

## A3.1 General solving rules — done
Done in `feat/coach-agent-files`.
- `coach/general/skills/solving-rules/SKILL.md`. Topics: decimals and rounding, SI units, answer format, always compute in Python, state assumptions, check rule references
Done when: Gion has reviewed it.

## A3.2 Log use skill — done
Done in `feat/coach-agent-files`; tool names follow A4.3.
- `coach/general/skills/log-use/SKILL.md`: join the shared live session; before each question, read every member's answers to it and the lessons for its topic; write an entry after the quick answer, the team answer and each review
- Entry fields: session, question number, problem (or the question text in a live quiz), agent, mode (quick / team / review), answer, result (correct / wrong / unknown; unknown during a live quiz), approach, what went wrong, why, rule for next time, feedback (which of the other answers are right and why)
- How: MCP tools when the agent supports them, otherwise print the entry for the member to paste into the app form
Done when: Gion has reviewed it.

## A3.3 Shared calculation scripts
Moved to A6.3: filled from solved problems after the trial, not written up front.

## A3.5 Quick and team answers — done
Done in `feat/coach-agent-files`.
- `coach/general/skills/solve-modes/SKILL.md`: both modes on every question, made for the live quiz where nobody knows the answer yet (Gion, 2026-10-14). Members join one live session. A quick answer from one agent, logged at once; then a team of 2–3 sub-agents solves independently, compares its answer with every answer the other members logged for that question, and logs which is right and why; each new disagreeing answer triggers a re-check and a review entry, until the answers agree or time is up; the agent says what to submit. Practice on past problems works the same way, with the FS Quiz answer used only afterwards. Web chats do the same steps one after another
Done when: Gion has reviewed it.

## A3.4 Competition rules — **Gion**
One branch per competition: `feat/competition-<event>`
- `COMPETITION.md` and `skills/` from Gion's text. Expected topics: quiz format, decimals, time limit, scoring, answer submission rules
Done when: Gion confirms the file says what they wrote.
