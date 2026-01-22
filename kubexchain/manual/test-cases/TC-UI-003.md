# Test Case: Error Handling

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-UI-003 |
| **Module** | UI |
| **Sub-Module** | Error Handling |
| **Test Priority** | High |
| **Test Type** | Negative |

---

## Test Objective

Verify that error messages are displayed correctly.

---

## Test Cases

| Scenario | Expected Error |
|----------|----------------|
| 404 page | "Page not found" |
| 500 error | "Server error" |
| Network failure | "Connection error" |
| Timeout | "Request timeout" |
| Invalid route | 404 page |

---

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Access invalid URL | 404 page shows |
| 2 | Force server error | Error message |
| 3 | Disconnect network | Offline message |
| 4 | Timeout request | Timeout message |

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Tester | | | |
