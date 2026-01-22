# Test Case: Password Reset

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-AUTH-003 |
| **Module** | Authentication |
| **Sub-Module** | Password Reset |
| **Test Priority** | High |
| **Test Type** | Functional |
| **Created By** | QA Team |
| **Created Date** | 2026-01-20 |
| **Last Updated** | 2026-01-21 |

---

## Test Objective

Verify that users can reset their password via email.

---

## Pre-requisites

- User account exists
- Access to user's email inbox

---

## Test Data

| Field | Value |
|-------|-------|
| Email | `testuser_reset@test.com` |
| New Password | `NewTest@654321` |

---

## Test Steps

| Step | Action | Expected Result | Pass/Fail |
|------|--------|-----------------|-----------|
| 1 | Navigate to https://kubexchain.com/forgot-password | Forgot password page loads | [ ] |
| 2 | Enter registered email | Email field accepts input | [ ] |
| 3 | Click "Send Reset Link" | Loading spinner appears | [ ] |
| 4 | Check email for reset link | Email received within 5 minutes | [ ] |
| 5 | Click reset link | Password reset page loads with new password fields | [ ] |
| 6 | Enter new password | Password strength indicator shows valid | [ ] |
| 7 | Confirm new password | Fields match | [ ] |
| 8 | Click "Reset Password" | Success message displayed | [ ] |
| 9 | Login with new password | Login successful, redirected to dashboard | [ ] |

---

## Notes

- Reset link should expire after 24 hours
- Password must meet complexity requirements

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Tester | | | |
| Reviewer | | | |
