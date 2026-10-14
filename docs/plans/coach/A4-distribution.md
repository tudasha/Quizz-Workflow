# A4. Distribution
Works without the quiz app. The app later reuses these outputs.

## A4.1 Setup prompt
Branch: `feat/setup-prompt`
- `SETUP_PROMPT.md` template; one generated prompt per competition, e.g.:
  "Clone <repo> (or git pull), read AGENTS.md, and use general/ and competitions/fsa/ for every problem I give you. Pull before each problem and push a log entry to the log branch after each one."
Done when: a member pastes it into Claude Code and the agent follows it.

## A4.2 Zip per competition
Branch: `feat/zip-build`
- GitHub Action on push to `main`: builds `<event>.zip` = `general/` + `competitions/<event>/` (+ `AGENTS.md`), published as release assets with a fixed "latest" link
Done when: downloading `fsa.zip` and uploading it to a Claude Project lets the agent solve with the same rules.

## A4.3 Log entries from agents without git
Branch: `feat/log-issue-form`
- GitHub issue form "Log entry" where the member pastes the agent's text
- Action validates the fields, commits the entry to `log`, closes the issue
- Replaced later by the app's log form (app task 7.4)
Done when: a pasted entry lands on `log` as one file.
