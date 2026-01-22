# Test Case: Deposit Amount Validation

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-DEPOSIT-002 |
| **Module** | Deposits |
| **Sub-Module** | Amount Validation |
| **Test Priority** | High |
| **Test Type** | Negative |
| **Created By** | QA Team |
| **Created Date** | 2026-01-21 |

---

## Test Objective

Verify deposit amount validation for all edge cases.

---

## Test Cases

| Test | Amount | Expected Error |
|------|--------|----------------|
| Below minimum | $5 | "Minimum deposit is $10" |
| Above maximum | $100,000 | "Maximum deposit is $50,000" |
| Zero amount | $0 | "Amount required" |
| Negative amount | $-100 | "Invalid amount" |
| Non-numeric | `abc` | "Invalid number" |
| Too many decimals | $100.123 | "Maximum 2 decimals" |

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Tester | | | |
