# Test Case: User Login

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-AUTH-002 |
| **Module** | Authentication |
| **Sub-Module** | User Login |
| **Test Priority** | High |
| **Test Type** | Functional |
| **Created By** | QA Team |
| **Created Date** | 2026-01-20 |
| **Last Updated** | 2026-01-21 |

---

## Test Objective

Verify that registered users can successfully log in to their account.

---

## Pre-requisites

- User account exists and is verified
- Account is not locked
- Correct credentials available

---

## Test Data

| Field | Value |
|-------|-------|
| Username/Email | `testuser_login@test.com` |
| Password | `Test@123456` |

---

## Test Steps

| Step | Action | Expected Result | Pass/Fail |
|------|--------|-----------------|-----------|
| 1 | Navigate to https://kubexchain.com/login | Login page loads with email and password fields | [ ] |
| 2 | Enter valid email | Email field accepts input | [ ] |
| 3 | Enter valid password | Password field masks input | [ ] |
| 4 | Click "Login" button | Loading spinner appears | [ ] |
| 5 | Wait for response | Redirect to dashboard/profile page | [ ] |
| 6 | Verify user is logged in | Welcome message or user avatar visible | [ ] |

---

## Test Environment

| Field | Value |
|-------|-------|
| Browser | Chrome 120+ |
| Operating System | Windows 11/macOS |
| Screen Resolution | 1920x1080 |

---

## Test Execution

| Field | Value |
|-------|-------|
| Executed By | QA Tester |
| Execution Date | |
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

- Test both email and username login if supported
- Check "Remember Me" functionality
- Verify session persistence

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Tester | | | |
| Reviewer | | | |
