# Test Case: User Registration

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-AUTH-001 |
| **Module** | Authentication |
| **Sub-Module** | User Registration |
| **Test Priority** | High |
| **Test Type** | Functional |
| **Created By** | QA Team |
| **Created Date** | 2026-01-20 |
| **Last Updated** | 2026-01-20 |

---

## Test Objective

Verify that new users can successfully register with email and password.

---

## Pre-requisites

- Test user account does not exist
- Access to email for verification
- Stable internet connection

---

## Test Data

| Field | Value |
|-------|-------|
| Username | `testuser_reg_001` |
| Email | `testuser_reg_001@kubexchain.test` |
| Password | `Test@123456` |
| Referral Code | (Optional) |

---

## Test Steps

| Step | Action | Expected Result | Pass/Fail |
|------|--------|-----------------|-----------|
| 1 | Navigate to https://kubexchain.com/register | Registration page loads with form fields | [ ] |
| 2 | Enter valid username: `testuser_reg_001` | Username field accepts input | [ ] |
| 3 | Enter valid email: `testuser_reg_001@kubexchain.test` | Email field accepts input | [ ] |
| 4 | Enter valid password: `Test@123456` | Password field accepts input with strength indicator | [ ] |
| 5 | Confirm password: `Test@123456` | Password confirmation matches | [ ] |
| 6 | Click "Create Account" button | Loading spinner appears | [ ] |
| 7 | Wait for response | Success message displayed: "Registration successful! Please verify your email." | [ ] |
| 8 | Check email inbox for verification link | Verification email received within 60 seconds | [ ] |
| 9 | Click verification link | Email verified successfully, redirect to login | [ ] |

---

## Test Environment

| Field | Value |
|-------|-------|
| Browser | Chrome |
| Browser Version | 120.0 |
| Operating System | Windows 11 |
| Screen Resolution | 1920x1080 |

---

## Test Execution

| Field | Value |
|-------|-------|
| Executed By | QA Tester |
| Execution Date | 2026-01-20 |
| Environment | Staging |

---

## Test Results

| Status | Result |
|--------|--------|
| [ ] Pass | All steps executed successfully |
| [ ] Fail | One or more steps failed |
| [ ] Blocked | Test cannot be executed |

---

## Actual Results

[To be filled during execution]

---

## Defects/Bugs Found

| Defect ID | Description | Severity | Status |
|-----------|-------------|----------|--------|
| N/A | | | |

---

## Notes

- Password must be at least 6 characters
- Username must be 3-30 characters
- Email must be unique

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Tester | | | |
| Reviewer | | | |
