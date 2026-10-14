# Repo hygiene

- Never commit build output or binaries (`dist/`, `build/`, `node_modules/`, `.venv/`, `*.zip`, compiled files). Release builds go in GitHub Releases.
- Never commit secrets: passwords, API keys, the admin passkey, database URLs. They live in environment variables; `.env` is in `.gitignore`, `.env.example` lists the names only.
- Shared code is reused through a package or submodule, never copied in.
- The AI coach knowledge repo is separate. The app serves its zips and hosts the log; the repo's content is not copied into this repo.
