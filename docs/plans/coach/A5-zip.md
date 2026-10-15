# A5. One zip for all competitions

The only way members get the coach material: one zip with every competition in its own folder.

## A5.1 Zip build — done (GitHub Release until R2 exists)
Done in `feat/coach-import`: `general/tools/build_zip.py` and the Coach zip Action.
- GitHub Action on push to `main` that changes `coach/`: builds `fs-quiz-coach.zip` from `coach/` = `AGENTS.md` + `LOG.md` + `general/` + `competitions/<event>/` for every event, with only the current-year rules and handbooks (older years left out)
- For now the zip replaces the files of the `coach-latest` GitHub Release (fixed download link); `VERSION.txt` inside says the commit and date
- Later: also upload the zip and the search index (A4.9) to the app's file storage (R2). The app at runtime only reads storage, so it needs no GitHub access (the R2 write key is a GitHub secret)
Done when: a new commit on `main` produces a fresh zip in storage.

## A5.2 LOG.md
First version done (`coach/LOG.md`: Claude Code, Gemini CLI, paste fallback). Branch for the rest: `feat/log-instructions`
- How to connect the log: MCP URL and token, with steps for Claude Projects, Claude Code, ChatGPT and Gemini; fallback: print the entry and paste it into the app form
- For Claude Code and Codex: a ready config for a local markdown MCP over the unzipped folder
Done when: a member follows it on each agent type without help.

## A5.3 Download page
Branch: `feat/coach-download`. After A4.1.
- One download button for the latest zip and its version
- Per competition, a Copy button with a short prompt: "Use competitions/<event>/ for every problem I give you"
- Shows the member's MCP URL and token status
Done when: e2e downloads the zip and copies the FSA prompt.

## A5.4 Size check — done
- If the zip is bigger than `zip_split_above_mb` in `config.json` (25 MB, for agents with a small upload limit such as Claude Project knowledge), the build also makes one zip per competition

## A5.5 Files for web chats — done
Gemini and other web chats can't open a zip (review, 2026-10-15). `general/tools/chat_files.py`, run by the zip build, writes Markdown files next to the zip on the `coach-latest` release:
- Per competition: `fs-quiz-coach-<event>-chat.md` (AGENTS.md, LOG.md, solving-rules, log-use, solve-modes, quiz-maker, COMPETITION.md, competition skills, KEY-VALUES), `fs-quiz-coach-<event>-handbook-<year>.md` (with its index) and `fs-quiz-coach-<event>-problems.md` (problems, solutions, newest first)
- Shared: `fs-quiz-coach-rules-<year>.md` (FS Rules with index and changes)
- No PDFs, images or third-party skills; each coach file is a section headed "File: <path>" so the paths in AGENTS.md still lead somewhere
Done when: a web chat given the chat, rules and handbook files answers a past problem by the solving rules.
