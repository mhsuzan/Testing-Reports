# Test Case: Registration Validation

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-AUTH-005 |
| **Module** | Authentication |
| **Sub-Module** | Registration Validation |
| **Test Priority** | High |
| **Test Type** | Negative |
| **Created By** | QA Team |
| **Created Date** | 2026-01-21 |

---

## Test Objective

Verify registration form validation for all edge cases.

---

## Test Cases

| Test | Input | Expected Error |
|------|-------|----------------|
| Short username | `ab` | "Minimum 3 characters" |
| Long username | 31 chars | "Maximum 30 characters" |
| Special chars in username | `user@name!` | "Invalid characters" |
| Weak password | `123` | "Minimum 8 characters" |
| No number in password | `abcdefgh` | "Must include number" |
| Email already exists | existing@test.com | "Email already registered" |
| Username already taken | existinguser | "Username taken" |

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Tester | | | |
