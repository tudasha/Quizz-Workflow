# A5. Zip per competition

The only way members get the coach material.

## A5.1 Zip build
Branch (coach repo): `feat/zip-build`
- GitHub Action on push to `main`: builds `<event>.zip` = `AGENTS.md` + `general/` + `competitions/<event>/` + `LOG.md`
- Uploads the zips to the app's file storage (R2) with a version number
Done when: a new commit on `main` produces fresh zips in storage.

## A5.2 LOG.md
Branch (coach repo): `feat/log-instructions`
- How to connect the log: MCP URL and token, with steps for Claude Projects, Claude Code, ChatGPT and Gemini; fallback: print the entry and paste it into the app form
Done when: a member follows it on each agent type without help.

## A5.3 Download page
Branch (this repo): `feat/coach-download`. After A4.1.
- Page listing competitions with the latest zip and its version; shows the member's MCP URL and token status
Done when: e2e downloads `fsa.zip`.
