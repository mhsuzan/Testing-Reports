# Test Case: Deposit Payment Flow

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-DEPOSIT-003 |
| **Module** | Deposits |
| **Sub-Module** | Payment Flow |
| **Test Priority** | High |
| **Test Type** | Functional |
| **Created By** | QA Team |
| **Created Date** | 2026-01-21 |

---

## Test Objective

Verify the complete deposit payment flow works correctly.

---

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to /invest | Page loads |
| 2 | Enter amount: $500 | Rate: 0.25% displayed |
| 3 | Select USDT/TRC20 | Currency/network selected |
| 4 | Click Invest Now | Payment gateway opens |
| 5 | Complete payment | Payment processing |
| 6 | Success page | "Deposit initiated" message |
| 7 | Check in history | Transaction added |
| 8 | Wait for approval | Status changes to "approved" |
| 9 | Check investments | Deposit appears in list |

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Tester | | | |
