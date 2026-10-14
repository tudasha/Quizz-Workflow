# 7. AI coach panel
Builds on Part A: log service (A4) and zips (A5) already exist.

## 7.1 Competition selector
Branch: `feat/coach-competitions`
- Competition list from the zips in storage; remembers the member's last choice
Done when: e2e: picking a competition shows its zip and the log for it.

## 7.2 Coach page
Branch: `feat/coach-page`. After 7.1.
- One page: zip download, MCP URL, token request and status, paste form, my log entries
- Replaces the A5.3 download page and the A4.5 form page
Done when: e2e covers download, token request and a pasted entry.

## 7.3 Log browser
Branch: `feat/log-browser`. After 7.1.
- All members can read log entries by competition, problem and topic, with review status
Done when: e2e filters by topic.
