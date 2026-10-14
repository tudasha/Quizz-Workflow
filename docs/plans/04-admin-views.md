# 4. Admin views
All pages and actions use `requireAdmin()`.

## 4.1 Departments
Branch: `feat/admin-departments`
- Users grouped by department; assign a user without one, move to another department, delete user (with confirm)
Done when: e2e covers move and delete.

## 4.2 Assignments
Branch: `feat/admin-assignments`
- Problems per user, with quiz, problem and date/time of assignment; filter by user and quiz
Done when: e2e shows an assignment made in 3.4.

## 4.3 All answers
Branch: `feat/admin-answers`
- Answers grouped by problem, with user, value and time
- Similar answers highlighted using one function in `src/lib/answer-similarity.ts`
- Default until decided: numbers equal within 1% relative tolerance (units stripped), text equal after trim and lower case
Done when: unit tests for the similarity function.

## 4.4 Answer similarity — **Decision**
Open: exact, numeric tolerance or AI. Only `answer-similarity.ts` changes once decided.
