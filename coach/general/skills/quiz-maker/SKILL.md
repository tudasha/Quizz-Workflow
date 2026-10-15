---
name: quiz-maker
description: Make a practice quiz for one Formula Student competition in that competition's own style - question types, topics, time limits and answer format taken from COMPETITION.md, the handbook's quiz section and its past problems - in English, with SVG figures where needed, every answer computed in Python and checked by a blind second solve; works with or without the app. Use when a member asks for a practice quiz, mock quiz or new questions for a competition or topic.
---

# Making a practice quiz

A practice quiz should feel like the real one for that competition: same kinds of questions, same topics, same time pressure, same answer format. The member takes it; you write it, grade it and explain it.

## 1. Ask, or pick a default
- Competition: required (a folder in `competitions/`).
- Number of questions: default 10.
- Topics: the ones the member names, or their weak topics from the dashboard (without the app, ask the member). Otherwise the competition's usual mix (step 2).
- Run: one question at a time with a timer (default), or a sheet with all questions and the answers at the end.
- Language: questions, options and answers in English, as in the real quiz; explanations in the member's language.

## 2. Learn the competition's style
Read, in this order, and note what you find:
1. `competitions/<event>/COMPETITION.md`: quiz format, time limits, decimals, scoring, event specifics. It wins over everything below.
2. The handbook's quiz section: search `competitions/<event>/handbook/current/` for "quiz" (e.g. FSG DE 3.1). Number of questions, time, scoring, who may answer.
3. The past problems: count question types, topics and time limits over `competitions/<event>/problems/*/problem.md`, most recent years first, e.g.

```python
import collections, glob, yaml
types, topics, times = collections.Counter(), collections.Counter(), []
for path in glob.glob("competitions/<event>/problems/*/problem.md"):
    text = open(path, encoding="utf-8").read()
    fields = yaml.safe_load(text[4:text.find("\n---\n", 4)])
    if (fields.get("year") or 0) >= 2024:
        types[fields["type"]] += 1
        topics.update(fields.get("topic") or [])
        times += [fields["time_s"]] if fields.get("time_s") else []
print(types, topics, sorted(times))
```

   No code execution (web chat): count by hand over the competition's problems file instead.
4. Read 3 to 5 recent past problems per chosen topic, with their `solution.md`, to see how questions are worded, how much text and how many steps they take, and how the answer is asked for.

Match that mix: if the competition asks mostly input questions with 2 decimals, so does your quiz.

## 3. Write the questions
Three kinds, mixed:
- **Variant** of a past problem: same method, new numbers or a changed condition (e.g. rear instead of front axle). Never copy a past problem as is: the member may have seen it.
- **Rules**: from this year's FS Rules and the competition handbook, with the rule number. Prefer rules that teams often get wrong and the handbook's event procedures and scoring formulas.
- **New calculation** on the competition's topics, in the same style and length as its past problems.

For each question:
- Givens with units, realistic for an FS car (`solving-rules` step 3), and exactly what is asked: unit, decimals, rounding.
- Type and time limit as in that competition.
- The answer, from a Python script you ran (`solving-rules`). Keep the script.
- Choice questions: options built from real mistakes, each one a wrong path someone could take (diameter as radius, km/h left unconverted, last year's rule, per wheel instead of per axle). Use traps from the log's lessons when there are any. Single-choice: exactly one option is right. Multi-choice: judge every option.
- Rule references, topic, and a short explanation of the right path and of the trap behind each wrong option.
- Rules and values from this year's files (`solving-rules`, "Never break these"), never from memory.

### Figures
Many real questions carry a figure: a circuit, a free-body diagram, a track layout, a plot or a table. Draw one when the question needs it:
- As SVG, with every value the question needs written on it, units included, and nothing that gives the answer away.
- Terminal agent: save it as `practice/<event>-<date>-q<n>.svg` and link it in the question. Web chat: show the SVG in the answer or as an artifact, or describe the figure in words if neither works.
- The blind second solve (step 4) gets the figure too: if it can't read a value from it, fix the figure.

## 4. Check every question
- Blind second solve: a sub-agent (or, in a web chat, a fresh solve without looking back) gets only the question as the member will see it and solves it by `solving-rules`.
- Same answer after rounding: keep it. Different: find why. Fix the question if it was unclear or the givens were missing, or fix the answer if yours was wrong. Can't settle it: drop the question and write a new one.
- Read it as the member: one clear meaning, nothing in the text gives the answer away, solvable within the time limit.

## 5. Run it
- Practice session: `start_session(competition, year)` (`log-use`).
- One at a time: show the question and its time limit, wait for the member's answer, then say right or wrong with the explanation. `record_answer` for each.
- Sheet: all questions first, the answers and explanations after the member hands in.
- At the end: score, time, results per topic, and the two or three things to practise next.
- A new trap the member fell into goes to the log as a lesson (`log-use`, `problem_id: note`).

### Without the app (no MCP)
- No session or `record_answer`: keep the score yourself, one line per question (number, topic, the member's answer, right or wrong, time).
- At the end, print that table and the lesson entries as YAML blocks (`log-use`, "Without MCP") for the member to paste into the app later.

## Keep apart
- Generated questions are practice only. Never add them to `competitions/<event>/problems/`: that folder holds real FS Quiz questions.
- Don't use the hidden test set, and don't write questions meant to copy it.
- The member can keep the quiz: in a terminal agent, save it as `practice/<event>-<date>.md` with the answers in a separate `practice/<event>-<date>-answers.md`.
