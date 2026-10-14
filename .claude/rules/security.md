# Security

- Admin rights come from a server-side role. The admin passkey is checked on the server, never in the client.
- Every admin action (delete, relocate, mark available, approve API tokens, review log entries) checks the role on the server.
- Assigning a problem to another user checks that the username exists, on the server.
- Passwords are hashed with a standard library (bcrypt or argon2), never stored or logged in plain text.
- All SQL uses parameters, never string concatenation.
- API tokens are stored hashed, shown once, revocable; every API and MCP call checks the token on the server.
