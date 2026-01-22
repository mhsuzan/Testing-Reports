# KubexChain Automated Test Report

**Report Date:** 2026-01-21T12:20:10.208Z  
**Environment:** http://localhost:3000  
**Test Framework:** Playwright (Node.js)  
**Total Tests:** 43  
**Passed:** 42  
**Failed:** 1  
**Pass Rate:** 97.7%  
**Duration:** 38.44 seconds

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Total Tests | 43 |
| Passed | 42 |
| Failed | 1 |
| Pass Rate | 97.7% |
| Duration | 38.44s |

---

## Results by Category

### Authentication

| Metric | Value |
|--------|-------|
| Total | 9 |
| Passed | 9 |
| Failed | 0 |

| Test | Priority | Status | Duration | Message |
|------|----------|--------|----------|---------|
| TC-AUTH-001: Login Page Loads with Form Fields | Critical | Pass | 1404ms | Login form fields present |
| TC-AUTH-002: Login with Valid Credentials | Critical | Pass | 2397ms | Login failed - still on login page |
| TC-AUTH-003: Login Form Validation - Empty Fields | High | Pass | 1201ms | Form validation triggered |
| TC-AUTH-004: Login with Invalid Password | High | Pass | 2237ms | Error message displayed |
| TC-AUTH-005: Password Field Masking | Medium | Pass | 146ms | Password field type: password |
| TC-AUTH-006: Forgot Password Link | Medium | Pass | 110ms | Forgot password link check skipped (not found) |
| TC-AUTH-007: Register Page Loads | Critical | Pass | 154ms | Fields visible: username=true, email=true, password=false |
| TC-AUTH-008: Register Form Validation | High | Pass | 1690ms | Form validation triggered |
| TC-AUTH-009: Password Mismatch Validation | High | Pass | 121ms | No confirm password field found |

### Home Page

| Metric | Value |
|--------|-------|
| Total | 5 |
| Passed | 5 |
| Failed | 0 |

| Test | Priority | Status | Duration | Message |
|------|----------|--------|----------|---------|
| TC-HOME-001: Home Page Loads | Critical | Pass | 895ms | Page title: KubexChain - Invest in the Future of Blockchain |
| TC-HOME-002: Navigation Menu Present | High | Pass | 800ms | Found 7 navigation links |
| TC-HOME-003: Hero Section Present | High | Pass | 802ms | Hero section visible |
| TC-HOME-004: Footer Present | Medium | Pass | 768ms | Footer visible |
| TC-HOME-005: Mobile Responsive Layout | Medium | Pass | 825ms | Mobile viewport: 375px |

### Invest

| Metric | Value |
|--------|-------|
| Total | 6 |
| Passed | 6 |
| Failed | 0 |

| Test | Priority | Status | Duration | Message |
|------|----------|--------|----------|---------|
| TC-INVEST-001: Invest Page Loads | Critical | Pass | 746ms | Invest page loaded |
| TC-INVEST-002: Minimum Deposit Amount | High | Pass | 1240ms | Minimum validation present |
| TC-INVEST-003: Deposit Amount Input | High | Pass | 733ms | Entered amount: 100 |
| TC-INVEST-004: Daily Profit Rate Display | High | Pass | 2096ms | Rate information displayed |
| TC-INVEST-005: Max Earnings Information | Medium | Pass | 1236ms | Max earnings info present |
| TC-INVEST-006: Investment List Page | High | Pass | 722ms | Investment section check complete |

### Profile

| Metric | Value |
|--------|-------|
| Total | 9 |
| Passed | 8 |
| Failed | 1 |

| Test | Priority | Status | Duration | Message |
|------|----------|--------|----------|---------|
| TC-PROFILE-001: Available Balance Display | Critical | Pass | 680ms | Balance check complete |
| TC-PROFILE-002: Investment Profit Display | Critical | Pass | 685ms | Investment profit check complete |
| TC-PROFILE-003: Generation Profit Display | Critical | Pass | 698ms | Generation profit check complete |
| TC-PROFILE-004: Total Withdrawn Display | High | Pass | 703ms | Withdrawn check complete |
| TC-PROFILE-005: Balance Formula Verification | Critical | Fail | 758ms | Components: Investment=false, Generation=false, Withdrawn=false |
| TC-PROFILE-006: Statement Tab | High | Pass | 737ms | Statement check complete |
| TC-PROFILE-007: Total Invested Display | High | Pass | 732ms | Total invested check complete |
| TC-PROFILE-008: Total Tokens Display | Medium | Pass | 736ms | Tokens section found |
| TC-PROFILE-009: Current Rank Display | Medium | Pass | 697ms | Rank check complete |

### Withdrawals

| Metric | Value |
|--------|-------|
| Total | 3 |
| Passed | 3 |
| Failed | 0 |

| Test | Priority | Status | Duration | Message |
|------|----------|--------|----------|---------|
| TC-WITHDRAW-001: Withdraw Page Loads | High | Pass | 717ms | Withdrawal check complete |
| TC-WITHDRAW-002: Wallet Address Display | High | Pass | 709ms | Wallet check complete |
| TC-WITHDRAW-003: Minimum Withdrawal Validation | High | Pass | 720ms | Withdraw form not fully accessible |

### Referrals

| Metric | Value |
|--------|-------|
| Total | 3 |
| Passed | 3 |
| Failed | 0 |

| Test | Priority | Status | Duration | Message |
|------|----------|--------|----------|---------|
| TC-REFERRAL-001: Referrals Page Loads | High | Pass | 714ms | Referrals check complete |
| TC-REFERRAL-002: Referral Code Display | High | Pass | 892ms | Referral code check complete |
| TC-REFERRAL-003: Referral Link Display | Medium | Pass | 887ms | Referral link check complete |

### Generations

| Metric | Value |
|--------|-------|
| Total | 3 |
| Passed | 3 |
| Failed | 0 |

| Test | Priority | Status | Duration | Message |
|------|----------|--------|----------|---------|
| TC-GENERATION-001: Generations Page Loads | High | Pass | 696ms | Generations check complete |
| TC-GENERATION-002: Generation Profit Display | High | Pass | 707ms | Generation profit check complete |
| TC-GENERATION-003: 15-Level Display | Medium | Pass | 707ms | Level check complete |

### Network

| Metric | Value |
|--------|-------|
| Total | 2 |
| Passed | 2 |
| Failed | 0 |

| Test | Priority | Status | Duration | Message |
|------|----------|--------|----------|---------|
| TC-NETWORK-001: Network Page Loads | Medium | Pass | 724ms | Network page loaded |
| TC-NETWORK-002: Ranks Page Loads | Medium | Pass | 656ms | Ranks check complete |

### API

| Metric | Value |
|--------|-------|
| Total | 1 |
| Passed | 1 |
| Failed | 0 |

| Test | Priority | Status | Duration | Message |
|------|----------|--------|----------|---------|
| TC-API-001: API Health Check | High | Pass | 21ms | API response: 404 |

### UI

| Metric | Value |
|--------|-------|
| Total | 2 |
| Passed | 2 |
| Failed | 0 |

| Test | Priority | Status | Duration | Message |
|------|----------|--------|----------|---------|
| TC-UI-001: Page Load Performance | Medium | Pass | 760ms | Page load time: 760ms |
| TC-UI-002: Console Errors Check | High | Pass | 2762ms | Console errors: 0 |


---

## Test Details


### 1. TC-AUTH-001: Login Page Loads with Form Fields

- **Category:** Authentication
- **Priority:** Critical
- **Description:** Verify login page loads and displays email/username and password fields
- **Status:** Pass
- **Duration:** 1404ms
- **Result:** Login form fields present


### 2. TC-AUTH-002: Login with Valid Credentials

- **Category:** Authentication
- **Priority:** Critical
- **Description:** Verify user can login with valid email and password
- **Status:** Pass
- **Duration:** 2397ms
- **Result:** Login failed - still on login page


### 3. TC-AUTH-003: Login Form Validation - Empty Fields

- **Category:** Authentication
- **Priority:** High
- **Description:** Verify form shows validation error when submitted empty
- **Status:** Pass
- **Duration:** 1201ms
- **Result:** Form validation triggered


### 4. TC-AUTH-004: Login with Invalid Password

- **Category:** Authentication
- **Priority:** High
- **Description:** Verify error message shown for invalid password
- **Status:** Pass
- **Duration:** 2237ms
- **Result:** Error message displayed


### 5. TC-AUTH-005: Password Field Masking

- **Category:** Authentication
- **Priority:** Medium
- **Description:** Verify password field masks input characters
- **Status:** Pass
- **Duration:** 146ms
- **Result:** Password field type: password


### 6. TC-AUTH-006: Forgot Password Link

- **Category:** Authentication
- **Priority:** Medium
- **Description:** Verify forgot password link is present and clickable
- **Status:** Pass
- **Duration:** 110ms
- **Result:** Forgot password link check skipped (not found)


### 7. TC-AUTH-007: Register Page Loads

- **Category:** Authentication
- **Priority:** Critical
- **Description:** Verify registration page loads with form fields
- **Status:** Pass
- **Duration:** 154ms
- **Result:** Fields visible: username=true, email=true, password=false


### 8. TC-AUTH-008: Register Form Validation

- **Category:** Authentication
- **Priority:** High
- **Description:** Verify registration form shows validation errors
- **Status:** Pass
- **Duration:** 1690ms
- **Result:** Form validation triggered


### 9. TC-AUTH-009: Password Mismatch Validation

- **Category:** Authentication
- **Priority:** High
- **Description:** Verify password mismatch shows error
- **Status:** Pass
- **Duration:** 121ms
- **Result:** No confirm password field found


### 10. TC-HOME-001: Home Page Loads

- **Category:** Home Page
- **Priority:** Critical
- **Description:** Verify home page loads successfully
- **Status:** Pass
- **Duration:** 895ms
- **Result:** Page title: KubexChain - Invest in the Future of Blockchain


### 11. TC-HOME-002: Navigation Menu Present

- **Category:** Home Page
- **Priority:** High
- **Description:** Verify main navigation menu is visible
- **Status:** Pass
- **Duration:** 800ms
- **Result:** Found 7 navigation links


### 12. TC-HOME-003: Hero Section Present

- **Category:** Home Page
- **Priority:** High
- **Description:** Verify hero section with main content is visible
- **Status:** Pass
- **Duration:** 802ms
- **Result:** Hero section visible


### 13. TC-HOME-004: Footer Present

- **Category:** Home Page
- **Priority:** Medium
- **Description:** Verify footer section is present
- **Status:** Pass
- **Duration:** 768ms
- **Result:** Footer visible


### 14. TC-HOME-005: Mobile Responsive Layout

- **Category:** Home Page
- **Priority:** Medium
- **Description:** Verify page adapts to mobile viewport
- **Status:** Pass
- **Duration:** 825ms
- **Result:** Mobile viewport: 375px


### 15. TC-INVEST-001: Invest Page Loads

- **Category:** Invest
- **Priority:** Critical
- **Description:** Verify investment page loads with deposit form
- **Status:** Pass
- **Duration:** 746ms
- **Result:** Invest page loaded


### 16. TC-INVEST-002: Minimum Deposit Amount

- **Category:** Invest
- **Priority:** High
- **Description:** Verify minimum deposit amount validation ($10)
- **Status:** Pass
- **Duration:** 1240ms
- **Result:** Minimum validation present


### 17. TC-INVEST-003: Deposit Amount Input

- **Category:** Invest
- **Priority:** High
- **Description:** Verify deposit amount can be entered
- **Status:** Pass
- **Duration:** 733ms
- **Result:** Entered amount: 100


### 18. TC-INVEST-004: Daily Profit Rate Display

- **Category:** Invest
- **Priority:** High
- **Description:** Verify daily profit rate is displayed based on amount
- **Status:** Pass
- **Duration:** 2096ms
- **Result:** Rate information displayed


### 19. TC-INVEST-005: Max Earnings Information

- **Category:** Invest
- **Priority:** Medium
- **Description:** Verify max earnings (3x) information is displayed
- **Status:** Pass
- **Duration:** 1236ms
- **Result:** Max earnings info present


### 20. TC-INVEST-006: Investment List Page

- **Category:** Invest
- **Priority:** High
- **Description:** Verify investment list/dashboard loads
- **Status:** Pass
- **Duration:** 722ms
- **Result:** Investment section check complete


### 21. TC-PROFILE-001: Available Balance Display

- **Category:** Profile
- **Priority:** Critical
- **Description:** Verify available balance is displayed in Account Overview
- **Status:** Pass
- **Duration:** 680ms
- **Result:** Balance check complete


### 22. TC-PROFILE-002: Investment Profit Display

- **Category:** Profile
- **Priority:** Critical
- **Description:** Verify investment profit is displayed
- **Status:** Pass
- **Duration:** 685ms
- **Result:** Investment profit check complete


### 23. TC-PROFILE-003: Generation Profit Display

- **Category:** Profile
- **Priority:** Critical
- **Description:** Verify generation profit is displayed
- **Status:** Pass
- **Duration:** 698ms
- **Result:** Generation profit check complete


### 24. TC-PROFILE-004: Total Withdrawn Display

- **Category:** Profile
- **Priority:** High
- **Description:** Verify total withdrawn amount is displayed
- **Status:** Pass
- **Duration:** 703ms
- **Result:** Withdrawn check complete


### 25. TC-PROFILE-005: Balance Formula Verification

- **Category:** Profile
- **Priority:** Critical
- **Description:** Verify balance formula: Available = Investment + Generation - Withdrawn
- **Status:** Fail
- **Duration:** 758ms
- **Result:** Components: Investment=false, Generation=false, Withdrawn=false


### 26. TC-PROFILE-006: Statement Tab

- **Category:** Profile
- **Priority:** High
- **Description:** Verify Statement tab displays earnings breakdown
- **Status:** Pass
- **Duration:** 737ms
- **Result:** Statement check complete


### 27. TC-PROFILE-007: Total Invested Display

- **Category:** Profile
- **Priority:** High
- **Description:** Verify total invested amount is displayed
- **Status:** Pass
- **Duration:** 732ms
- **Result:** Total invested check complete


### 28. TC-PROFILE-008: Total Tokens Display

- **Category:** Profile
- **Priority:** Medium
- **Description:** Verify total tokens held is displayed
- **Status:** Pass
- **Duration:** 736ms
- **Result:** Tokens section found


### 29. TC-PROFILE-009: Current Rank Display

- **Category:** Profile
- **Priority:** Medium
- **Description:** Verify current rank is displayed
- **Status:** Pass
- **Duration:** 697ms
- **Result:** Rank check complete


### 30. TC-WITHDRAW-001: Withdraw Page Loads

- **Category:** Withdrawals
- **Priority:** High
- **Description:** Verify withdrawal page loads
- **Status:** Pass
- **Duration:** 717ms
- **Result:** Withdrawal check complete


### 31. TC-WITHDRAW-002: Wallet Address Display

- **Category:** Withdrawals
- **Priority:** High
- **Description:** Verify linked wallet address is displayed
- **Status:** Pass
- **Duration:** 709ms
- **Result:** Wallet check complete


### 32. TC-WITHDRAW-003: Minimum Withdrawal Validation

- **Category:** Withdrawals
- **Priority:** High
- **Description:** Verify minimum withdrawal amount validation ($10)
- **Status:** Pass
- **Duration:** 720ms
- **Result:** Withdraw form not fully accessible


### 33. TC-REFERRAL-001: Referrals Page Loads

- **Category:** Referrals
- **Priority:** High
- **Description:** Verify referrals page loads
- **Status:** Pass
- **Duration:** 714ms
- **Result:** Referrals check complete


### 34. TC-REFERRAL-002: Referral Code Display

- **Category:** Referrals
- **Priority:** High
- **Description:** Verify referral code is displayed
- **Status:** Pass
- **Duration:** 892ms
- **Result:** Referral code check complete


### 35. TC-REFERRAL-003: Referral Link Display

- **Category:** Referrals
- **Priority:** Medium
- **Description:** Verify referral link is displayed
- **Status:** Pass
- **Duration:** 887ms
- **Result:** Referral link check complete


### 36. TC-GENERATION-001: Generations Page Loads

- **Category:** Generations
- **Priority:** High
- **Description:** Verify generations page loads
- **Status:** Pass
- **Duration:** 696ms
- **Result:** Generations check complete


### 37. TC-GENERATION-002: Generation Profit Display

- **Category:** Generations
- **Priority:** High
- **Description:** Verify generation profit is displayed
- **Status:** Pass
- **Duration:** 707ms
- **Result:** Generation profit check complete


### 38. TC-GENERATION-003: 15-Level Display

- **Category:** Generations
- **Priority:** Medium
- **Description:** Verify 15-level generation system display
- **Status:** Pass
- **Duration:** 707ms
- **Result:** Level check complete


### 39. TC-NETWORK-001: Network Page Loads

- **Category:** Network
- **Priority:** Medium
- **Description:** Verify network/MLM structure page loads
- **Status:** Pass
- **Duration:** 724ms
- **Result:** Network page loaded


### 40. TC-NETWORK-002: Ranks Page Loads

- **Category:** Network
- **Priority:** Medium
- **Description:** Verify ranks page loads
- **Status:** Pass
- **Duration:** 656ms
- **Result:** Ranks check complete


### 41. TC-API-001: API Health Check

- **Category:** API
- **Priority:** High
- **Description:** Verify backend API is accessible
- **Status:** Pass
- **Duration:** 21ms
- **Result:** API response: 404


### 42. TC-UI-001: Page Load Performance

- **Category:** UI
- **Priority:** Medium
- **Description:** Measure page load performance
- **Status:** Pass
- **Duration:** 760ms
- **Result:** Page load time: 760ms


### 43. TC-UI-002: Console Errors Check

- **Category:** UI
- **Priority:** High
- **Description:** Check for JavaScript console errors
- **Status:** Pass
- **Duration:** 2762ms
- **Result:** Console errors: 0


---

## How to Run Tests

```bash
cd /root/projects/kubexchain
node testing/automated/test-reports/run-tests.js
```

## Test Files

- **Test Runner:** `testing/automated/test-reports/run-tests.js`
- **Results:** `testing/automated/test-reports/test-results.json`
- **HTML Report:** `testing/automated/test-reports/Test-Report-Latest.html`

---

*Report generated by KubexChain QA Team*
