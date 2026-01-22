# Test Case: Max Earnings Cap

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-DEPOSIT-007 |
| **Module** | Deposits |
| **Sub-Module** | Earnings Cap |
| **Test Priority** | High |
| **Test Type** | Functional |

---

## Test Objective

Verify that maximum earnings cap (3x) works correctly.

---

## Test Data

| Deposit | $1,000 |
| Max Earnings | $3,000 |

---

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create deposit $1,000 | Max shown: $3,000 |
| 2 | Wait 2 years or until 3x | No more profits |
| 3 | Check status | Marked "Completed" |
| 4 | Verify no further profit | Balance stops growing |

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Tester | | | |
