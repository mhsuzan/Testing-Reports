# Test Case: Create Deposit

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-DEPOSIT-001 |
| **Module** | Deposits |
| **Sub-Module** | Create Deposit |
| **Test Priority** | High |
| **Test Type** | Functional |
| **Created By** | QA Team |
| **Created Date** | 2026-01-20 |
| **Last Updated** | 2026-01-20 |

---

## Test Objective

Verify that users can create a deposit and the system calculates daily profits correctly based on deposit amount.

---

## Pre-requisites

- User must be logged in
- User must have sufficient balance or be making a new deposit
- User must complete payment

---

## Test Data

| Field | Value |
|-------|-------|
| Username | `testuser_deposit_001` |
| Deposit Amount | $100 |
| Expected Daily Rate | 0.25% |
| Expected Daily Profit | $0.25 |
| Max Earnings (3x) | $300 |

---

## Test Steps

| Step | Action | Expected Result | Pass/Fail |
|------|--------|-----------------|-----------|
| 1 | Login with `testuser_deposit_001` | Dashboard loads successfully | [ ] |
| 2 | Navigate to Invest page | Investment options displayed | [ ] |
| 3 | Select deposit amount: $100 | Amount field updated, rate shown: 0.25% | [ ] |
| 4 | Verify daily profit display | Shows: $0.25/day | [ ] |
| 5 | Verify max earnings display | Shows: $300.00 (3x cap) | [ ] |
| 6 | Select currency (USDT) | Currency selected | [ ] |
| 7 | Select network (TRC20) | Network selected | [ ] |
| 8 | Click "Invest Now" | Payment modal/gateway opens | [ ] |
| 9 | Complete payment | Payment processing indicator | [ ] |
| 10 | Wait for confirmation | Success message: "Deposit initiated" | [ ] |
| 11 | Wait for admin approval | Status changes to "approved" | [ ] |
| 12 | Navigate to Profile > Investments | Deposit listed with details | [ ] |
| 13 | Verify deposit details | Amount: $100, Daily Rate: 0.25%, Status: Approved | [ ] |
| 14 | Check after 24 hours | Daily profit added: $0.25 | [ ] |

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

## Expected Daily Profit Rates

| Deposit Amount | Daily Rate | Daily Profit (per $100) |
|----------------|------------|------------------------|
| $10 - $500 | 0.25% | $0.25 |
| $501 - $2,000 | 0.30% | $0.30 |
| $2,001 - $5,000 | 0.35% | $0.35 |
| $5,001 - $10,000 | 0.40% | $0.40 |
| $10,001+ | 0.45% | $0.45 |

---

## Defects/Bugs Found

| Defect ID | Description | Severity | Status |
|-----------|-------------|----------|--------|
| N/A | | | |

---

## Notes

- Maximum earnings capped at 3x deposit amount
- Deposit must be approved by admin before earning profits
- Profit accrues daily at midnight (cron job)

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Tester | | | |
| Reviewer | | | |
