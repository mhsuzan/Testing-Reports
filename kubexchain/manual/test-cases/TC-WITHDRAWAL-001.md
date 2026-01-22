# Test Case: Withdrawal Request

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-WITHDRAWAL-001 |
| **Module** | Withdrawals |
| **Sub-Module** | Create Withdrawal |
| **Test Priority** | High |
| **Test Type** | Functional |
| **Created By** | QA Team |
| **Created Date** | 2026-01-20 |
| **Last Updated** | 2026-01-20 |

---

## Test Objective

Verify that users can request withdrawals from their available balance.

---

## Pre-requisites

- User must be logged in
- User must have linked wallet address
- User must have sufficient available balance

---

## Test Data

| Field | Value |
|-------|-------|
| Username | `testuser_withdraw_001` |
| Wallet Address | `0x742d35Cc6634C0532925a3b844Bc9e7595f8fE45` |
| Available Balance | ≥ $10 |
| Withdrawal Amount | $50 |

---

## Test Steps

| Step | Action | Expected Result | Pass/Fail |
|------|--------|-----------------|-----------|
| 1 | Login with `testuser_withdraw_001` | Dashboard loads successfully | [ ] |
| 2 | Navigate to Withdraw page | Withdraw form displayed | [ ] |
| 3 | Verify wallet address is linked | Wallet address shown: `0x742d...` | [ ] |
| 4 | Check available balance displayed | Balance: ≥$10 | [ ] |
| 5 | Enter withdrawal amount: $50 | Amount field updated | [ ] |
| 6 | Click "Request Withdrawal" | Confirmation modal appears | [ ] |
| 7 | Confirm withdrawal request | Success message: "Withdrawal request submitted" | [ ] |
| 8 | Check transaction history | Transaction shows: Pending -$50 | [ ] |
| 9 | Check available balance | Balance reduced by $50 | [ ] |
| 10 | Wait for admin processing | Status changes to "completed" | [ ] |
| 11 | Verify wallet transaction | Amount transferred to wallet | [ ] |

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

## Withdrawal Validation Rules

| Scenario | Amount | Expected Result |
|----------|--------|-----------------|
| Minimum withdrawal | < $10 | Error: Minimum withdrawal is $10 |
| Insufficient balance | > Available | Error: Insufficient balance |
| No wallet linked | N/A | Error: Please link wallet first |
| Valid amount | $10 - Balance | Success |

---

## Defects/Bugs Found

| Defect ID | Description | Severity | Status |
|-----------|-------------|----------|--------|
| N/A | | | |

---

## Notes

- Minimum withdrawal: $10
- Withdrawal processing time: 24-48 hours
- Wallet must be linked before withdrawal

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Tester | | | |
| Reviewer | | | |
