# Test Case: Locked Balance Daily Profit

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-GENERATION-003 |
| **Module** | Generations |
| **Sub-Module** | Locked Balance |
| **Test Priority** | High |
| **Test Type** | Functional |
| **Created By** | QA Team |
| **Created Date** | 2026-01-21 |

---

## Test Objective

Verify that locked generation balance earns 0.10% daily profit.

---

## Test Data

| Field | Value |
|-------|-------|
| Locked Balance | $500 |
| Daily Rate | 0.10% |
| Daily Profit | $0.50 |

---

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to Generations | Locked balance displayed |
| 2 | Check locked balance | Amount visible |
| 3 | Check daily rate | 0.10% shown |
| 4 | Wait 24 hours | Profit increases by $0.50 |
| 5 | Check after 7 days | Profit ~$3.50 added |
| 6 | Verify withdrawability | Profit can be withdrawn |

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Tester | | | |
