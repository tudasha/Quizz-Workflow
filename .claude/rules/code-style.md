# Code style

- Indentation: 4 spaces, no tabs (unless the chosen language's formatter enforces otherwise; then the formatter wins).
- Naming: `camelCase` or `snake_case` for variables and functions, following the language's convention, consistent within a file. `ALL_CAPS` for constants.
- Descriptive names: `assigned_problem_count`, not `apc`.
- Comments explain why, not what. Assume the reader knows the language but not your logic.
- Keep framework, database and network code apart from logic. Logic must be testable without a running server or database.
