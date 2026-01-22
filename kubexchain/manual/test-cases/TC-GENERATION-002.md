# Test Case: Generation Commission Levels

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-GENERATION-002 |
| **Module** | Generations |
| **Sub-Module** | Multi-Level |
| **Test Priority** | High |
| **Test Type** | Functional |
| **Created By** | QA Team |
| **Created Date** | 2026-01-21 |

---

## Test Objective

Verify all 15 generation levels work correctly with proper commission rates.

---

## Test Data

| Level | Rate | Test Deposit |
|-------|------|--------------|
| 1 | 8% | $1,000 → $80 |
| 2 | 5% | $1,000 → $50 |
| 3 | 3% | $1,000 → $30 |
| 4 | 2% | $1,000 → $20 |
| 5 | 2% | $1,000 → $20 |
| 6-15 | 1% | $1,000 → $10 each |

---

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Navigate to Generations | All levels visible |
| 2 | Expand Level 1 details | Commission breakdown shown |
| 3 | Expand Level 2 details | Commission breakdown shown |
| 4 | Check Level 3-15 | All levels accessible |
| 5 | Verify commission rates | Rates match structure |
| 6 | Check total commissions | Sum of all levels |

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Tester | | | |
