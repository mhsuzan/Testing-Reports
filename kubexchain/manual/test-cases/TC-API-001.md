# Test Case: API Health Check

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-API-001 |
| **Module** | API |
| **Sub-Module** | Health Check |
| **Test Priority** | High |
| **Test Type** | Functional |
| **Created By** | QA Team |
| **Created Date** | 2026-01-21 |

---

## Test Objective

Verify that the backend API is accessible and responding.

---

## Test Endpoints

| Endpoint | Method | Expected Result |
|----------|--------|-----------------|
| /api/health | GET | 200 OK |
| /api/users | GET | User data returned |
| /api/deposits | GET | Deposit data returned |

---

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Call health endpoint | Response: 200 |
| 2 | Check response time | < 500ms |
| 3 | Verify data format | JSON correct |
| 4 | Test authentication | Token required |

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Tester | | | |
