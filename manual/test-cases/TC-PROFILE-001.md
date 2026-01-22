# Test Case: Profile Balance Calculation

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-PROFILE-001 |
| **Module** | Profile |
| **Sub-Module** | Balance Calculation |
| **Test Priority** | Critical |
| **Test Type** | Functional |
| **Created By** | QA Team |
| **Created Date** | 2026-01-20 |
| **Last Updated** | 2026-01-20 |

---

## Test Objective

Verify that the profile page correctly displays:
- Available Balance
- Investment Profit
- Generation Profit
- Total Withdrawals

Using the formula:
```
Available Balance = Investment Profit + Generation Profit - Total Withdrawals
```

---

## Pre-requisites

- User with existing deposits
- User with generation earnings
- User with withdrawal history

---

## Test Data

| Field | Value |
|-------|-------|
| Username | `rashedul01` |
| Deposit Amount | $10 |
| Investment Profit | $1.18 |
| Generation Profit | $43.97 |
| Total Withdrawals | $0 |
| Expected Available Balance | $45.15 |

---

## Test Steps

| Step | Action | Expected Result | Pass/Fail |
|------|--------|-----------------|-----------|
| 1 | Login with `rashedul01` | Dashboard loads | [ ] |
| 2 | Navigate to Profile page | Profile page displays | [ ] |
| 3 | Locate Account Overview section | Balance cards visible | [ ] |
| 4 | Check Available Balance | Displays: $45.15 | [ ] |
| 5 | Check Investment Profit | Displays: $1.18 | [ ] |
| 6 | Check Generation Profit | Displays: $43.97 | [ ] |
| 7 | Check Total Withdrawals | Displays: $0.00 | [ ] |
| 8 | Verify formula | Available = Investment + Generation - Withdrawals | [ ] |
| 9 | Compare with Statement tab | Values match across tabs | [ ] |

---

## Test Environment

| Field | Value |
|-------|-------|
| Browser | Chrome |
| Browser Version | 120.0 |
| Operating System | Windows 11 |

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

## Balance Verification Table

| Component | Expected | Actual | Match |
|-----------|----------|--------|-------|
| Available Balance | $45.15 | | [ ] |
| Investment Profit | $1.18 | | [ ] |
| Generation Profit | $43.97 | | [ ] |
| Total Withdrawals | $0.00 | | [ ] |

---

## Generation Profit Calculation

| Commission | Date | Days | Daily Rate | Profit |
|------------|------|------|------------|--------|
| $400.80 | Dec 5, 2025 | 46 | 0.10% | $18.44 |
| $400.80 | Dec 5, 2025 | 46 | 0.10% | $18.44 |
| $50.10 | Dec 5, 2025 | 46 | 0.10% | $2.30 |
| ... | ... | ... | ... | ... |
| **Total** | | | | **$43.97** |

---

## Defects/Bugs Found

| Defect ID | Description | Severity | Status |
|-----------|-------------|----------|--------|
| N/A | | | |

---

## Notes

- Generation profit is calculated as: `commissionAmount × 0.001 × days_since_created`
- Investment profit is sum of `deposit.totalEarned`
- Withdrawals are summed from completed withdrawal transactions

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Tester | | | |
| Reviewer | | | |
