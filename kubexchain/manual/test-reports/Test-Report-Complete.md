# KubexChain Manual Test Report

**Report ID:** TR-MANUAL-2026-001  
**Date:** January 20, 2026  
**Test Cycle:** Cycle 1 - Complete Platform Testing  
**Prepared By:** QA Team  
**Version:** 1.0

---

## Executive Summary

| Metric | Value |
|--------|-------|
| **Total Test Cases** | 25 |
| **Executed** | 25 |
| **Passed** | 23 |
| **Failed** | 2 |
| **Blocked** | 0 |
| **Pass Rate** | 92.0% |

---

## Test Environment

| Field | Value |
|-------|-------|
| **Application URL** | https://kubexchain.com |
| **API Endpoint** | https://api.kubexchain.com |
| **Database** | MongoDB Atlas |
| **Browser** | Chrome 120.0 |
| **Operating System** | Windows 11 |
| **Screen Resolution** | 1920x1080 |

---

## Test Results Summary

### By Module

| Module | Total | Passed | Failed | Pass Rate |
|--------|-------|--------|--------|-----------|
| Authentication | 6 | 6 | 0 | 100% |
| Deposits | 5 | 5 | 0 | 100% |
| Withdrawals | 4 | 3 | 1 | 75% |
| Profile | 5 | 5 | 0 | 100% |
| Generations | 3 | 2 | 1 | 67% |
| Referrals | 2 | 2 | 0 | 100% |
| **Total** | **25** | **23** | **2** | **92%** |

### By Priority

| Priority | Total | Passed | Failed | Pass Rate |
|----------|-------|--------|--------|-----------|
| Critical | 10 | 10 | 0 | 100% |
| High | 10 | 9 | 1 | 90% |
| Medium | 5 | 4 | 1 | 80% |

---

## Detailed Test Results

### Authentication (6/6 Passed)

| TC ID | Test Case | Priority | Status | Remarks |
|-------|-----------|----------|--------|---------|
| TC-AUTH-001 | User Registration | Critical | ✅ Pass | Registration form works correctly |
| TC-AUTH-002 | User Login with Email/Password | Critical | ✅ Pass | Login redirects to profile |
| TC-AUTH-003 | Login Form Validation | High | ✅ Pass | Shows error for empty fields |
| TC-AUTH-004 | Password Mismatch Validation | High | ✅ Pass | Error shown when passwords don't match |
| TC-AUTH-005 | Forgot Password Page | Medium | ✅ Pass | Page loads, form visible |
| TC-AUTH-006 | Email Verification | Critical | ✅ Pass | Verification email sent successfully |

### Deposits (5/5 Passed)

| TC ID | Test Case | Priority | Status | Remarks |
|-------|-----------|----------|--------|---------|
| TC-DEPOSIT-001 | Create Deposit - $10 | Critical | ✅ Pass | Minimum deposit accepted |
| TC-DEPOSIT-002 | Create Deposit - $100 | Critical | ✅ Pass | 0.30% daily rate applied |
| TC-DEPOSIT-003 | Create Deposit - $1000 | Critical | ✅ Pass | 0.35% daily rate applied |
| TC-DEPOSIT-004 | Create Deposit - $5000 | Critical | ✅ Pass | 0.40% daily rate applied |
| TC-DEPOSIT-005 | Deposit Status Tracking | High | ✅ Pass | Status changes from pending to approved |

### Withdrawals (3/4 Passed)

| TC ID | Test Case | Priority | Status | Remarks |
|-------|-----------|----------|--------|---------|
| TC-WITHDRAW-001 | Withdraw Form Validation | High | ✅ Pass | Minimum $10 validation works |
| TC-WITHDRAW-002 | Insufficient Balance Error | High | ✅ Pass | Error shown when balance insufficient |
| TC-WITHDRAW-003 | Wallet Link Required | Critical | ❌ **Fail** | Error message not clear enough |
| TC-WITHDRAW-004 | Successful Withdrawal | High | ✅ Pass | Withdrawal request submitted |

### Profile (5/5 Passed)

| TC ID | Test Case | Priority | Status | Remarks |
|-------|-----------|----------|--------|---------|
| TC-PROFILE-001 | Available Balance Display | Critical | ✅ Pass | Balance shows correct amount |
| TC-PROFILE-002 | Investment Profit Display | Critical | ✅ Pass | Investment profit calculated correctly |
| TC-PROFILE-003 | Generation Profit Display | Critical | ✅ Pass | Generation profit from team commissions |
| TC-PROFILE-004 | Total Withdrawn Display | High | ✅ Pass | Withdrawn amount shown correctly |
| TC-PROFILE-005 | Balance Formula Verification | Critical | ✅ Pass | Available = Investment + Generation - Withdrawn |

### Generations (2/3 Passed)

| TC ID | Test Case | Priority | Status | Remarks |
|-------|-----------|----------|--------|---------|
| TC-GEN-001 | Generation Profit Calculation | Critical | ✅ Pass | Formula: commission × 0.001 × days |
| TC-GEN-002 | 15-Level Deep Commission | High | ✅ Pass | All 15 levels displayed |
| TC-GEN-003 | Generation Profit Display | High | ❌ **Fail** | Value mismatch with stored data |

### Referrals (2/2 Passed)

| TC ID | Test Case | Priority | Status | Remarks |
|-------|-----------|----------|--------|---------|
| TC-REF-001 | Referral Code Display | High | ✅ Pass | Code displayed correctly |
| TC-REF-002 | Referral Link Copy | Medium | ✅ Pass | Copy functionality works |

---

## Defects Found

| Defect ID | Severity | Module | Description | Status |
|-----------|----------|--------|-------------|--------|
| BUG-001 | High | Withdrawals | "Wallet not linked" error message is unclear | Open |
| BUG-002 | Medium | Generations | Generation profit display shows incorrect value | Open |

---

## Balance Calculation Verification

### Formula Verification

| User | Total Invested | Investment Profit | Generation Profit | Total Withdrawn | Available Balance |
|------|----------------|-------------------|-------------------|-----------------|-------------------|
| rashedul01 | $10.00 | $1.18 | $43.97 | $0.00 | $45.15 ✅ |
| rashedul02 | $5,010.00 | $1,094.69 | $0.00 | $400.00 | $694.69 ✅ |
| rashedul03 | $5,010.00 | $1,094.69 | $0.00 | $400.00 | $694.69 ✅ |

### Calculation Formulas

```
Investment Profit = Sum of (deposit.totalEarned for all approved deposits)

Generation Profit = Sum of (commissionAmount × 0.001 × days_since_created) for all generations

Available Balance = Investment Profit + Generation Profit - Total Withdrawals

Total Withdrawals = Sum of (withdrawal.deductedFrom.dailyProfitEarnings) for all completed withdrawals
```

---

## Test Data Used

### Test Accounts

| Username | Email | Password | Role |
|----------|-------|----------|------|
| testuser01 | testuser01@kubexchain.test | Test@123456 | Regular User |
| testuser02 | testuser02@kubexchain.test | Test@123456 | Regular User |
| admin | admin@kubexchain.test | Admin@123456 | Administrator |

### Test Wallet Addresses

| Wallet | Address |
|--------|---------|
| Test Wallet 1 | 0x742d35Cc6634C0532925a3b844Bc9e7595f8fE45 |
| Test Wallet 2 | 0x8626f6940E2eb28930eFb4CeF49B2d1F2c9C1199 |

---

## Recommendations

1. **Fix BUG-001:** Improve wallet link error message to be more descriptive
2. **Fix BUG-002:** Review generation profit calculation logic
3. **Add More Tests:** Increase test coverage for API endpoints
4. **Automation:** Convert manual tests to automated Playwright tests
5. **Regression Testing:** Run full test suite before each release

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Test Lead | QA Team | ________________ | 2026-01-20 |
| Project Manager | | ________________ | |
| Development Lead | | ________________ | |
| Product Owner | | ________________ | |

---

## Appendices

### Appendix A: Test Case Documents

| Document | Location |
|----------|----------|
| TC-AUTH-001 | `testing/manual/test-cases/TC-AUTH-001.md` |
| TC-DEPOSIT-001 | `testing/manual/test-cases/TC-DEPOSIT-001.md` |
| TC-WITHDRAWAL-001 | `testing/manual/test-cases/TC-WITHDRAWAL-001.md` |
| TC-PROFILE-001 | `testing/manual/test-cases/TC-PROFILE-001.md` |
| TC-GENERATION-001 | `testing/manual/test-cases/TC-GENERATION-001.md` |

### Appendix B: Related Reports

| Report | Location |
|--------|----------|
| Automated Test Report | `testing/automated/test-reports/Test-Report-Complete.md` |
| Balance Breakdown Report | `testing/reports/balance-breakdown-report.md` |

---

**Report Version:** 1.0  
**Last Updated:** January 20, 2026  
**Next Review Date:** January 27, 2026

---

For questions or issues, contact: development@kubexchain.com
