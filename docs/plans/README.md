# Build plan

One file per step. Do the steps in order; tasks inside a step can run in parallel unless a task says "after".

## How to work a task
- One task = one branch = one PR into `dev`. Branch name is given in the task.
- Read the task's "Done when" before starting; that is the acceptance test.
- Write the tests first where the task has logic (skill `tdd`).
- PR title starts with the task number, e.g. `3.4 Assign problem to another user`.
- A task marked **Decision** needs Gion's answer first. Do not decide it.

## Steps
1. [Setup](01-setup.md)
2. [Accounts](02-accounts.md)
3. [Quizzes and problems](03-quizzes-problems.md)
4. [Admin views](04-admin-views.md)
5. [Notifications and status](05-notifications.md)
6. [Documentation page](06-documentation.md)
7. [AI coach panel](07-ai-coach-panel.md)
8. [Tutorial](08-tutorial.md) (last)
