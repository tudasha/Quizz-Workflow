# 3. Quizzes and problems

## 3.1 Home: quiz list
Branch: `feat/quiz-list`
- List of quizzes (title, competition, problem count, completed count)
- Admin: create, rename, delete quiz
Done when: e2e: admin creates a quiz, member sees it but has no edit controls.

## 3.2 Problem gallery
Branch: `feat/problem-gallery`. After 3.1.
- Cards ordered by number; badge: Available, `N Assigned`, Completed; final answer shown once completed
- Highlights: red = assigned to me, gold = my department (via assignee departments), green = completed and relevant to me
- Hover preview of the problem image
- Highlight rules live in `src/lib/` as one pure function
Done when: unit tests cover every highlight rule; e2e shows correct badges.

## 3.3 Problem admin and image upload
Branch: `feat/problem-admin`. After 3.2.
- Admin: add problem (number, title, image), edit title, delete
- Images uploaded to R2 through a server-signed URL; only image types, size limit
Done when: e2e: admin adds a problem with an image, it appears in the gallery.

## 3.4 Problem detail and assignment
Branch: `feat/assignment`. After 3.2.
- Detail page: image, title, assignees
- Assign to me; assign to another user (username checked on the server; clear error if not found); unassign
- Creates a notification for the assignee (used in step 5)
Done when: e2e covers assign to me, assign to unknown username (error), unassign.

## 3.5 Answer submission
Branch: `feat/answers`. After 3.4.
- One answer per user per problem; resubmit updates it (`updated_at` changes)
Done when: unit test on the upsert; e2e: submit, resubmit, one row remains.

## 3.6 Completed and available
Branch: `feat/problem-status`. After 3.5.
- Mark as Completed with a final answer; Mark as Available (admin only)
Done when: e2e: completed problem shows the final answer and green highlight.

## 3.7 AI check of answers — **Decision**
Open: which model and API, and how the confidence tag is computed.
Done when: Gion decides; then split into tasks here.
