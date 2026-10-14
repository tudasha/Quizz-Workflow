# A5. One zip for all competitions

The only way members get the coach material: one zip with every competition in its own folder.

## A5.1 Zip build
Branch: `feat/zip-build`
- GitHub Action on push to `main` that changes `coach/`: builds `fs-quiz-coach.zip` from `coach/` = `AGENTS.md` + `LOG.md` + `general/` + `competitions/<event>/` for every event, with only the current-year rules and handbooks (older years left out)
- Uploads the zip and the search index (A4.9) to the app's file storage (R2) with a version number. The app at runtime only reads storage, so it needs no GitHub access (the R2 write key is a GitHub secret)
Done when: a new commit on `main` produces a fresh zip in storage.

## A5.2 LOG.md
Branch: `feat/log-instructions`
- How to connect the log: MCP URL and token, with steps for Claude Projects, Claude Code, ChatGPT and Gemini; fallback: print the entry and paste it into the app form
- For Claude Code and Codex: a ready config for a local markdown MCP over the unzipped folder
Done when: a member follows it on each agent type without help.

## A5.3 Download page
Branch: `feat/coach-download`. After A4.1.
- One download button for the latest zip and its version
- Per competition, a Copy button with a short prompt: "Use competitions/<event>/ for every problem I give you"
- Shows the member's MCP URL and token status
Done when: e2e downloads the zip and copies the FSA prompt.

## A5.4 Size check
- If the zip is too big for an agent's upload limit (for example Claude Project knowledge), the build also makes one zip per competition as a fallback
