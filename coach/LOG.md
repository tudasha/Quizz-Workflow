# Connecting the shared log

The team's solve log and solve sessions live in the quiz workflow app. Your agent reads lessons and writes entries live through the app's MCP server. What to read and write is in `general/skills/log-use/`.

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
Use the agent as is. At the end of each problem it prints the log entry as a YAML block (see `general/skills/log-use/`); paste it into the Log entry form on the AI coach page.

## Tools the server offers
| Tool | Use |
|---|---|
| `get_lessons` | lessons for a competition, problem or topic |
| `add_log_entry` | write one entry after a problem |
| `start_session`, `record_answer` | keep score in a quiz run |
| `search_rules` | find a rule by number or phrase |
| `search_problems`, `get_problem` | find similar past problems and open one |
