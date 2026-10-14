# Testing and CI

- Every PR must pass CI (build, lint, tests) before merge.
- New logic comes with unit tests. Bug fixes come with a test that fails before the fix.
- Database changes go through migrations, never manual edits to a shared database.
- Never skip, disable or delete a test to get CI green.
