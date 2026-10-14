# Build plan

One file per step. Do the parts and steps in order; tasks inside a step can run in parallel unless a task says "after".

## How to work a task
- One task = one branch = one PR. Branch name is given in the task. App repo: PR into `dev`. Coach repo: PR into `main`.
- Read the task's "Done when" before starting; that is the acceptance test.
- Write the tests first where the task has logic (skill `tdd`).
- PR title starts with the task number, e.g. `3.4 Assign problem to another user`.
- A task marked **Decision** or **Gion** needs Gion first. Do not decide or do it.

## Part A: AI coach repo (first)
Separate repo. Tasks are done there; the plan lives here.
- A1. [Repo setup](coach/A1-repo-setup.md)
- A2. [Data import](coach/A2-data-import.md)
- A3. [Rules and skills](coach/A3-rules-skills.md)
- A4. [Distribution: setup prompt, zip, log entries](coach/A4-distribution.md)
- A5. [Trial and review](coach/A5-trial-review.md)

Part B starts only after Gion approves Part A (A5.4).

## Part B: Quiz workflow app
1. [Setup](01-setup.md)
2. [Accounts](02-accounts.md)
3. [Quizzes and problems](03-quizzes-problems.md)
4. [Admin views](04-admin-views.md)
5. [Notifications and status](05-notifications.md)
6. [Documentation page](06-documentation.md)
7. [AI coach panel](07-ai-coach-panel.md)
8. [Tutorial](08-tutorial.md) (last)
