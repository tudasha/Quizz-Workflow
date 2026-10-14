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

## 2.3 Admin role and passkey
Branch: `feat/admin-role`. After 2.1.
- Admin passkey field on login; checked on the server against `ADMIN_PASSKEY_HASH` (env); on match the user's role becomes `admin`
- One server helper `requireAdmin()` used by every admin route and action
- Wrong passkey: same error as wrong password, rate limited
Done when: unit tests for `requireAdmin`; e2e test: member cannot open admin pages or call admin actions.

## 2.4 Header
Branch: `feat/header`. After 2.1.
- Username badge, department, logout
Done when: logout ends the session and returns to `/login`.
