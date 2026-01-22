# KubexChain Testing Reports

This repository contains all test cases, test scripts, and reports for the KubexChain project.

## Repository Structure

```
Testing-Reports/
├── README.md
├── automated/
│   ├── test-cases/
│   │   ├── authentication.spec.ts
│   │   ├── deposits.spec.ts
│   │   ├── generations.spec.ts
│   │   ├── profile.spec.ts
│   │   ├── withdrawals.spec.ts
│   │   └── playwright.config.ts
│   └── test-reports/
│       ├── run-tests.js
│       ├── generate-report.js
│       ├── test-results.json
│       ├── Test-Report-2026-01-20.md
│       ├── Test-Report-Complete.md
│       └── Test-Report-Latest.html
├── manual/
│   ├── test-cases/
│   │   ├── TC-AUTH-001.md
│   │   ├── TC-DEPOSIT-001.md
│   │   ├── TC-GENERATION-001.md
│   │   ├── TC-PROFILE-001.md
│   │   └── TC-WITHDRAWAL-001.md
│   └── test-reports/
│       └── Test-Report-Complete.md
└── templates/
    ├── template-test-case.md
    ├── template-test-report.md
    └── template-bug-report.md
```

## Test Coverage

### Automated Tests (Playwright)
- **Authentication**: Login, registration, form validation
- **Deposits**: Investment creation, profit calculations
- **Generations**: Multi-level commission system
- **Profile**: User balance, earnings display
- **Withdrawals**: Withdrawal functionality

### Manual Test Cases
- TC-AUTH-001: Authentication flows
- TC-DEPOSIT-001: Deposit creation and profit calculation
- TC-GENERATION-001: Generation/MLM system
- TC-PROFILE-001: User profile and balance verification
- TC-WITHDRAWAL-001: Withdrawal process

## Running Automated Tests

```bash
# Navigate to test directory
cd automated/test-reports

# Run all tests
node run-tests.js

# Generate HTML report
node generate-report.js
```

## Latest Test Results

**Date**: 2026-01-21
**Total Tests**: 43
**Passed**: 42
**Failed**: 1
**Pass Rate**: 97.7%

### Results by Category
| Category | Passed | Total | Rate |
|----------|--------|-------|------|
| Authentication | 9 | 9 | 100% |
| Home Page | 5 | 5 | 100% |
| Invest | 6 | 6 | 100% |
| Profile | 8 | 9 | 89% |
| Withdrawals | 3 | 3 | 100% |
| Referrals | 3 | 3 | 100% |
| Generations | 3 | 3 | 100% |
| Network | 2 | 2 | 100% |
| API | 1 | 1 | 100% |
| UI | 2 | 2 | 100% |

## Investment Profit Rates

| Amount Range | Daily Rate |
|--------------|------------|
| $10 - $500 | 0.25% |
| $501 - $2,000 | 0.30% |
| $2,001 - $5,000 | 0.35% |
| $5,001 - $10,000 | 0.40% |
| $10,001+ | 0.45% |

## Generation Bonus (15 Levels)

| Level | Commission |
|-------|------------|
| 1 | 8% |
| 2 | 5% |
| 3 | 3% |
| 4 | 2% |
| 5 | 2% |
| 6-15 | 1% each |

## Notes

- Maximum earnings capped at 3x deposit amount
- Generation bonus is LOCKED (not withdrawable)
- Locked generation balance earns 0.10% daily (withdrawable)
- Daily profit calculation runs at midnight (cron job)

---
**Last Updated**: 2026-01-21
