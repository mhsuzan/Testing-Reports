# Test Case: Login Form Validation

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-AUTH-004 |
| **Module** | Authentication |
| **Sub-Module** | Form Validation |
| **Test Priority** | High |
| **Test Type** | Negative |
| **Created By** | QA Team |
| **Created Date** | 2026-01-21 |

---

## Test Objective

Verify that login form validation works correctly for all edge cases.

---

## Test Cases

| Test | Input | Expected Error |
|------|-------|----------------|
| Empty email | - | "Email is required" |
| Empty password | - | "Password is required" |
| Invalid email format | `notanemail` | "Invalid email format" |
| Wrong password | wrongpass | "Invalid credentials" |
| Non-existent email | `notfound@test.com` | "User not found" |

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Tester | | | |
