# Repo hygiene

- Never commit build output or binaries (`dist/`, `build/`, `node_modules/`, `.venv/`, `*.zip`, compiled files). Release builds go in GitHub Releases.
- Never commit secrets: passwords, API keys, the admin passkey, database URLs. They live in environment variables; `.env` is in `.gitignore`, `.env.example` lists the names only.
- Shared code is reused through a package or submodule, never copied in.
- The AI coach content lives in `coach/` in this repo (Gion, 2026-10-14). It is shipped to members as a zip; app code never imports from it.
