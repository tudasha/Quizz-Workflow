# A3. Rules and skills

Gion, 2026-10-14: Claude writes `AGENTS.md` and the general skills (A3.1, A3.2, A3.5), Gion reviews them. The per-competition rules (A3.4) come from Gion's text: agents format them, keep the wording and ask about gaps instead of filling them.

## A3.1 General solving rules — done
Done in `feat/coach-agent-files`.
- `coach/general/skills/solving-rules/SKILL.md`. Topics: decimals and rounding, SI units, answer format, always compute in Python, state assumptions, check rule references
Done when: Gion has reviewed it.

## A3.2 Log use skill — done
Done in `feat/coach-agent-files`; tool names follow A4.3.
- `coach/general/skills/log-use/SKILL.md`: before each problem, read the log entries for that problem and topic; after it, write one entry
- Entry fields: problem, agent, result (correct / wrong / unknown), approach, what went wrong, why, rule for next time
- How: MCP tools when the agent supports them, otherwise print the entry for the member to paste into the app form
Done when: Gion has reviewed it.

## A3.3 Shared calculation scripts
Moved to A6.3: filled from solved problems after the trial, not written up front.

## A3.5 Quick and deep solving — done
Done in `feat/coach-agent-files`.
- `coach/general/skills/solve-modes/SKILL.md`: quick mode (one agent, fast, for easy questions) and deep mode (coordinator plus sub-agents where the agent supports them; the quick answer is the reference)
Done when: Gion has reviewed it.

## A3.4 Competition rules — **Gion**
One branch per competition: `feat/competition-<event>`
- `COMPETITION.md` and `skills/` from Gion's text. Expected topics: quiz format, decimals, time limit, scoring, answer submission rules
Done when: Gion confirms the file says what they wrote.
