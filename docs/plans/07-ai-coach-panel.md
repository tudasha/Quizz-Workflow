# 7. AI coach panel
Builds on Part A: log service (A4) and zips (A5) already exist.

## 7.1 Competition selector
Branch: `feat/coach-competitions`
- Competition list from the zip's folders; picking one shows its copy prompt, log and dashboard numbers
Done when: e2e: picking a competition shows its prompt and log.

## 7.2 Coach page
Branch: `feat/coach-page`. After 7.1.
- One page: zip download, copy prompt per competition, MCP URL, token request and status, paste form, my sessions and log entries
- Replaces the A5.3 download page and the A4.5 form page
Done when: e2e covers download, token request and a pasted entry.

## 7.3 Log browser
Branch: `feat/log-browser`. After 7.1.
- All members can read log entries by competition, problem and topic, with review status
Done when: e2e filters by topic.

## 7.4 Agent answers on the problem — idea (Gion, 2026-10-16)
Not split into tasks yet.
- The quick agent logs its answer as soon as it has one and does not wait for the team (already the rule in the coach's `solve-modes`)
- The app takes that answer from the log and shows it right away on the matching problem of the quiz (part 3), marked as the quick answer
- Needs: a link from a live solve session and its question number to the app's quiz and problem
- Open: how the team answer and later reviews show next to it
Done when: Gion settles the open point; then split into tasks.
