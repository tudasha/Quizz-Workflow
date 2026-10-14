# 2. Accounts

## 2.1 Sign up and log in
Branch: `feat/auth`
- Better Auth with username + password; passwords hashed by Better Auth
- Pages: `/login`, `/signup`; errors shown inline
- Session cookie keeps the user logged in (auto-login) until logout or expiry
Done when: e2e test signs up, reloads the page and is still logged in.

## 2.2 Department on first login
Branch: `feat/first-login-department`. After 2.1.
- If `department_id` is empty after login, redirect to a picker; all other pages are blocked until it is set
Done when: e2e test: new user must pick a department before reaching Home.

## 2.3 Admin role
Branch: `feat/admin-role`. After 2.1.
- Every member has their own username and password; no passkey and no second login
- Admin (moderator) is a role on the account: the first admin comes from the seed script, admins can promote others
- Everyone can see every page; one server helper `requireAdmin()` guards admin actions only (edit, delete, review, approve)
Done when: unit tests for `requireAdmin`; e2e test: a member sees admin pages read-only and cannot call admin actions.

## 2.4 Header
Branch: `feat/header`. After 2.1.
- Username badge, department, logout
Done when: logout ends the session and returns to `/login`.
