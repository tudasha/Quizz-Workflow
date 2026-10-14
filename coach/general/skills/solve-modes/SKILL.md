---
name: solve-modes
description: Choose quick mode (one agent, fast) or deep mode (a coordinator with sub-agents that solve independently and check each other until they agree) for a Formula Student quiz problem. Use at the start of every problem.
---

# Quick and deep mode

## Which mode
- **Quick**: timed quizzes, easy or single-step questions, or when the member asks for speed.
- **Deep**: practice, multi-step calculations, rules questions with several rules involved, any answer with low confidence, or when the member asks.
- Quick never skips `solving-rules`: the number is still computed in Python and the format still checked.

## Quick mode
One agent solves once with `solving-rules` and answers. If confidence is low, say so and offer deep mode.

## Deep mode
The same member's agent checks itself by solving the problem more than once, independently.

1. **Reference**: solve in quick mode first. Keep this answer to yourself.
2. **Independent solvers**: start 2 or 3 sub-agents (`dispatching-parallel-agents`). Give each one the problem text, the competition folder, the relevant rules and `solving-rules`. Do not give them the reference answer or each other's work. Ask one of them to use a different method when one exists (e.g. energy instead of forces).
3. **Each solver returns**: final answer, method, the script it ran, rule references, confidence.
4. **Compare** the reference and all solver answers. They agree when they are equal after rounding to the required format.
5. **All agree**: answer with that result and say how many independent solutions matched.
6. **They differ**: find the first step where they split (a rule read differently, a unit, radius vs diameter, an assumption). Send that step back to the solvers that differ, with the other side's reasoning for that step only, and ask them to re-check it. Repeat at most 2 rounds.
7. **Still no agreement**: give the answer with the strongest reasoning, show the other one and why it was rejected, mark confidence low, and log it so a topic checker can review.

## Agents without sub-agents
Web chats (Claude Project, ChatGPT, Gemini) run the same steps one after another in the same conversation: solve, then solve again from scratch with a different method without looking at the first result, then compare as in steps 4 to 7.

## Log
Write one log entry per problem, not per solver. Put in `approach` how many solutions agreed and in `what_went_wrong` any step where they split.
