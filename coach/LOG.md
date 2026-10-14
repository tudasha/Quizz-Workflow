# Connecting the shared log

The team's solve log and solve sessions live in the quiz workflow app. Your agent reads lessons and the other members' answers and writes entries live through the app's MCP server; during a live quiz this is how the members' agents compare answers. What to read and write is in `general/skills/log-use/`.

## What you need
- **MCP URL**: `https://<app address>/api/mcp`. The exact address is on the AI coach page of the app.
- **Personal API token**: request it on the AI coach page; an admin approves it. It is shown once: keep it in your agent's settings, never in a chat, a file in this folder or a log entry.

## Claude Code
```bash
claude mcp add --transport http fs-quiz https://<app address>/api/mcp --header "Authorization: Bearer <your token>"
```
Check with `claude mcp list`.

## Gemini CLI
In `~/.gemini/settings.json`:
```json
{
  "mcpServers": {
    "fs-quiz": {
      "httpUrl": "https://<app address>/api/mcp",
      "headers": { "Authorization": "Bearer <your token>" }
    }
  }
}
```

## Other agents (Codex, Claude.ai, ChatGPT, Gemini web)
Add a remote MCP server with the URL above, if your agent and plan allow custom connectors. The AI coach page lists the steps that work for each agent once they are tested.

## No MCP
Use the agent as is. It prints each log entry as a YAML block (see `general/skills/log-use/`). During a live quiz, share it in the team chat and paste the other members' entries into your agent; afterwards paste every entry into the Log entry form on the AI coach page.

## Tools the server offers
| Tool | Use |
|---|---|
| `start_session`, `join_session` | open a live or practice session, or join one with its code |
| `get_answers` | every answer, review and feedback logged for a question in the session |
| `get_lessons` | lessons for a competition, topic or past problem |
| `add_log_entry` | write an entry after the quick answer, the team answer and each review |
| `record_answer` | keep score in the session |
| `search_rules` | find a rule by number or phrase |
| `search_problems`, `get_problem` | find similar past problems and open one |
