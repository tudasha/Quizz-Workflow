# 5. Notifications and status

## 5.1 Action toasts
Branch: `feat/toasts`
- Every action shows a toast for 3 seconds (success or error)
Done when: e2e sees a toast after assign and after submit.

## 5.2 "Assigned to you" notifications
Branch: `feat/live-notifications`. After 3.4.
- Server-Sent Events endpoint pushes new `notification` rows to the logged-in user
- Fallback: poll every 15 seconds if SSE is not available on the chosen host
- Several notifications are queued and shown one after another, 5 seconds each; marked read once shown
Done when: e2e with two browsers: A assigns to B, B sees the notification without reloading.

## 5.3 Connection status
Branch: `feat/connection-status`. After 5.2.
- Indicator from the SSE connection state: connected, reconnecting, offline
Done when: e2e: going offline in Playwright shows "offline".
