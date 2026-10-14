# 7. AI coach panel
Needs the AI coach knowledge repo (separate repo, see PROJECT_CONTEXT.md). The app reaches it through a GitHub App or token in env (`COACH_REPO`, `GITHUB_TOKEN`); never exposed to the browser.

## 7.1 Competition selector
Branch: `feat/coach-competitions`
- Lists the folders under `competitions/` in the coach repo (cached a few minutes)
Done when: unit test with a mocked GitHub API; page lists the competitions.

## 7.2 Setup prompt
Branch: `feat/coach-setup-prompt`. After 7.1.
- Prompt template filled with the repo URL and the chosen competition folder; Copy button
- Template text lives in one file so it can be edited without code changes
Done when: unit test on the template; e2e copies the prompt.

## 7.3 Zip download
Branch: `feat/coach-zip`. After 7.1.
- Server builds a zip of `general/` + `competitions/<chosen>/` from the repo's `main` and streams it
Done when: test checks the zip holds exactly those two folders.

## 7.4 Log entry form
Branch: `feat/coach-log-form`. After 7.1.
- Paste field for the log entry the agent wrote; checks required fields (result, approach, what went wrong, why, rule for next time)
- Commits one file to the coach repo's `log` branch: `log/<yyyy-mm-dd>-<username>-<problem>.md`, author = the member
Done when: unit test on validation; integration test with a mocked GitHub API.

## 7.5 Log push access
Branch: `feat/coach-log-access`. After 7.1.
- Member enters their GitHub username and requests push access; admin approves or rejects in an admin page
- On approval the app gives that GitHub user write access to the coach repo (`main` stays protected, so only `log` takes direct pushes)
Done when: e2e: request, admin approves, status shows approved.
