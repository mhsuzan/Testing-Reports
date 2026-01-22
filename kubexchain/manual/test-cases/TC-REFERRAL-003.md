# Test Case: Referral Commission

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-REFERRAL-003 |
| **Module** | Referrals |
| **Sub-Module** | Commission |
| **Test Priority** | High |
| **Test Type** | Functional |
| **Created By** | QA Team |
| **Created Date** | 2026-01-21 |

---

## Test Objective

Verify that referral commission (5% on first deposit) is calculated correctly.

---

## Test Data

| Field | Value |
|-------|-------|
| Referral Deposit | $500 |
| Commission Rate | 5% |
| Expected Commission | $25 |

---

## Test Steps

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | New user registers with referral code | Code tracked |
| 2 | New user makes first deposit: $500 | Deposit approved |
| 3 | Referrer checks earnings | Commission: $25 |
| 4 | Check commission source | Shows referral deposit |
| 5 | Second deposit by referral | No additional commission |
| 6 | Check total referral earnings | Correct total |

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Tester | | | |
