# A3. Rules and skills

Content comes from Gion. Agents do not write these rules or skills from scratch: they turn Gion's text into the file format (SKILL.md front matter, headings), keep the wording, and ask about gaps instead of filling them. Tasks marked **Gion** wait for that text.

## A3.1 General solving rules — **Gion**
Branch: `feat/skill-solving-rules`
- `general/skills/solving-rules/SKILL.md` from Gion's text. Expected topics: decimals and rounding, SI units, answer format, always compute in Python, state assumptions, check rule references
Done when: Gion confirms the file says what they wrote.

## A3.2 Log use skill — **Gion**
Branch: `feat/skill-log-use`. After A4.3.
- `general/skills/log-use/SKILL.md` from Gion's text: before each problem, read the log entries for that problem and topic; after it, write one entry
- Entry fields: problem, agent, result (correct / wrong / unknown), approach, what went wrong, why, rule for next time
- How: MCP tools when the agent supports them, otherwise print the entry for the member to paste into the app form
Done when: Gion confirms the file says what they wrote.

## A3.3 Shared calculation scripts
Moved to A6.3: filled from solved problems after the trial, not written up front.

## A3.5 Quick and deep solving — **Gion**
Branch: `feat/skill-solve-modes`
- Skill from Gion's text: quick mode (one agent, fast, for easy questions) and deep mode (coordinator plus sub-agents where the agent supports them; the quick answer is the reference)
Done when: Gion confirms the file says what they wrote.

## A3.4 Competition rules — **Gion**
One branch per competition: `feat/competition-<event>`
- `COMPETITION.md` and `skills/` from Gion's text. Expected topics: quiz format, decimals, time limit, scoring, answer submission rules
Done when: Gion confirms the file says what they wrote.
