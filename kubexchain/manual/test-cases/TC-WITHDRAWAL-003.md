# Test Case: Withdrawal Status Tracking

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-WITHDRAWAL-003 |
| **Module** | Withdrawals |
| **Sub-Module** | Status Tracking |
| **Test Priority** | High |
| **Test Type** | Functional |
| **Created By** | QA Team |
| **Created Date** | 2026-01-21 |

---

## Test Objective

Verify that withdrawal status is tracked correctly through all stages.

---

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Request withdrawal: $50 | Status: "Pending" |
| 2 | Check after 1 hour | Status unchanged |
| 3 | Admin processes | Status: "Processing" |
| 4 | Transaction complete | Status: "Completed" |
| 5 | Check transaction hash | Hash visible |
| 6 | Verify balance deducted | Balance updated |

---

## Withdrawal Status Flow

```
Pending -> Processing -> Completed
                \
                 -> Failed (with reason)
```

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Tester | | | |
