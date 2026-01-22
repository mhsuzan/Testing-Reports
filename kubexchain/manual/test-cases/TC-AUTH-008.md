# Test Case: Account Lockout

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-AUTH-008 |
| **Module** | Authentication |
| **Sub-Module** | Security |
| **Test Priority** | High |
| **Test Type** | Negative |

---

## Test Objective

Verify that account lockout works after multiple failed login attempts.

---

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Attempt wrong password 5 times | "Account locked" message |
| 2 | Try login during lockout | Access denied |
| 3 | Wait lockout period | Login allowed again |

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Tester | | | |
