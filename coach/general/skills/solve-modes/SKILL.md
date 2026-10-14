---
name: solve-modes
description: Every Formula Student quiz problem is solved twice - first a quick answer from one agent, logged at once, then a team of sub-agents that solves independently, compares its result with every answer in the log for that problem, and logs which answer is right and why. Use at the start of every problem.
---

# Quick answer, then team answer

Every problem gets both. The quick answer comes first, so the member has an answer within quiz time. The team answer comes after it and has the last word.

## 1. Quick answer
1. Read the log for this problem (`log-use`).
2. One agent solves once by `solving-rules`: givens with units, SI, Python, plausibility, format.
3. Give the member the answer at once, marked **Quick answer**, with confidence.
4. Write it to the log right away: an entry with `mode: quick` (`log-use`). In a quiz run, also `record_answer`.

Then start the team. Don't wait for the member.

## 2. Team answer
5. Start 2 or 3 sub-agents (`dispatching-parallel-agents`). Give each one the problem text, the competition folder, the relevant rules and `solving-rules`. Don't give them the quick answer, the answers in the log or each other's work. Ask one of them to use a different method when one exists (e.g. energy instead of forces).
6. Each sub-agent returns: final answer, method, the script it ran, rule references, confidence.
7. Compare the sub-agents. They agree when their answers are equal after rounding to the required format. When they differ, find the first step where they split (a rule read differently, a unit, radius vs diameter, an assumption). Send that step back to the ones that differ, with the other side's reasoning for that step only, and ask them to re-check it. At most 2 rounds.

## 3. Check the log again and compare
8. Read the log for this problem again. Answers that other members or agents wrote while the team worked count too.
9. Put side by side: the team answer, the quick answer, every other answer in the log for this problem, and the FS Quiz answer in `problem.md` when there is one (`status: unverified` means nobody on the team has checked it yet).
10. For each answer that differs from the team answer, find the first step where it went wrong. If an earlier answer has an argument the team missed, send that step to the sub-agents to re-check before deciding.

## 4. Final answer and feedback
11. Give the member the result, marked **Team answer**, with how many independent solutions matched. If it differs from the quick answer, say that first, plainly: the quick answer was wrong, this is the right one, and why.
12. Write a log entry with `mode: team`. Put the answer in `answer`. In `feedback` put the argument for the correct answer and, for every other answer in the log for this problem, whether it is right and why (e.g. "quick 12.5 kN wrong: took the diameter as the radius").
13. If the team still cannot agree, or disagrees with the FS Quiz answer, give the answer with the strongest reasoning, show the other one and why it was rejected, and mark confidence low. Say so in the entry so a topic checker reviews it.

Every later solve of the same problem, by any member, starts from these entries and adds its own. The log gets closer to the right answer each time, and a topic checker confirms it in the end.

## Agents without sub-agents
Web chats (Claude Project, ChatGPT, Gemini) do the same steps one after another in the same conversation:
- quick answer and its log entry
- two more solutions from scratch, each with a different method and without looking at the earlier ones
- then steps 8 to 13

## Timed quizzes
If time runs out, the member enters the quick answer. The team answer still finishes and is logged, so the next attempt and the other members benefit.
