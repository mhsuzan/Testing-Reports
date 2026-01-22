# Test Case: Investment Profit Tracking

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-DEPOSIT-004 |
| **Module** | Deposits |
| **Sub-Module** | Profit Tracking |
| **Test Priority** | High |
| **Test Type** | Functional |
| **Created By** | QA Team |
| **Created Date** | 2026-01-21 |

---

## Test Objective

Verify that investment profits are calculated and tracked correctly over time.

---

## Test Data

| Field | Value |
|-------|-------|
| Deposit Amount | $1,000 |
| Daily Rate | 0.30% |
| Daily Profit | $3.00 |
| Max Earnings | $3,000 |

---

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Create deposit: $1,000 | Deposit approved |
| 2 | Check immediately | Profit: $0.00 |
| 3 | Wait 24 hours | Profit: $3.00 |
| 4 | Wait 7 days | Profit: ~$21.00 |
| 5 | Check max progress | Progress bar updates |
| 6 | Check 30 days | Profit: ~$90.00 |
| 7 | Wait until 3x | Deposit marked "Completed" |

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Tester | | | |
