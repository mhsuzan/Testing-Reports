# Test Case: Withdrawal Validation

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-WITHDRAWAL-002 |
| **Module** | Withdrawals |
| **Sub-Module** | Validation |
| **Test Priority** | High |
| **Test Type** | Negative |
| **Created By** | QA Team |
| **Created Date** | 2026-01-21 |

---

## Test Objective

Verify withdrawal form validation for all edge cases.

---

## Test Cases

| Test | Amount | Expected Error |
|------|--------|----------------|
| Below minimum | $5 | "Minimum $10" |
| Above maximum | $100,000 | "Maximum $50,000" |
| Exceeds balance | $1,000,000 | "Insufficient balance" |
| No wallet linked | - | "Link wallet first" |
| Decimal too long | $100.123 | "Invalid amount" |

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Tester | | | |
