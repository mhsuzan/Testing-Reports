# Test Case: Session Management

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-AUTH-006 |
| **Module** | Authentication |
| **Sub-Module** | Session |
| **Test Priority** | High |
| **Test Type** | Functional |
| **Created By** | QA Team |
| **Created Date** | 2026-01-21 |

---

## Test Objective

Verify that session management works correctly.

---

## Test Cases

| Test | Action | Expected Result |
|------|--------|-----------------|
| Login persistence | Close browser, reopen | Still logged in |
| Logout | Click logout | Redirected to login |
| Session timeout | Wait for expiry | Warning shown |
| Protected route | Access without login | Redirected to login |
| Multiple devices | Login on 2nd device | First session active |

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Tester | | | |
