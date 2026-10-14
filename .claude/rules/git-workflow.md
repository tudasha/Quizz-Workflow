# Git workflow

## Branches
| Type | Prefix | Use | Merges into |
|---|---|---|---|
| Integration | `dev` | Active development and integration | `main` (lead only) |
| Feature | `feat/` | New functionality, e.g. `feat/problem-gallery` | `dev` |
| Bugfix | `fix/` | Bug fix, e.g. `fix/assign-username-check` | `dev` |
| Refactor | `refactor/` | Cleanup, no behaviour change | `dev` |
| Testing | `test/` | Experiments or new tests | `dev` |
| Docs | `docs/` | Documentation only | `dev` |

- Never push to `main` or `dev` directly. Always a PR from a prefixed branch into `dev`.
- A lead merges `dev` into `main` once `dev` is stable and tested on the deployed test environment.
- `main` is production-ready only: always safe to deploy.

## Commits
- One logical change per commit ("Add username check on assign", not "Work on app").
- Commit messages in English, imperative mood.

## Pull requests
- Open a draft PR early; it tells the team who is working on which module.
- At least one approval from a lead before merge.
- CI must be green before merge.

## Releases
- Every deploy to production is tagged (`v1.0.2`) with a GitHub Release.
