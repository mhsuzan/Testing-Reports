# KubexChain Testing Documentation

This folder contains all testing documentation for the KubexChain project.

## Folder Structure

```
testing/
├── README.md                    # This file
├── manual/                      # Manual testing documentation
│   ├── test-cases/             # Manual test case documents
│   │   ├── TC-AUTH-001.md
│   │   ├── TC-DEPOSIT-001.md
│   │   ├── TC-WITHDRAWAL-001.md
│   │   ├── TC-PROFILE-001.md
│   │   ├── TC-REFERRAL-001.md
│   │   └── TC-GENERATION-001.md
│   └── test-reports/           # Manual test execution reports (PDF)
│       ├── Test-Report-2026-01-01.pdf
│       └── Test-Report-Cycle-1.pdf
├── automated/                   # Automated testing documentation
│   ├── test-cases/             # Automated test scripts/cases
│   │   ├── authentication.spec.ts
│   │   ├── deposits.spec.ts
│   │   ├── withdrawals.spec.ts
│   │   ├── profile.spec.ts
│   │   └── README.md
│   └── test-reports/           # Automated test execution reports (PDF)
│       ├── Automated-Test-Report-2026-01-01.pdf
│       └── Cypress-Test-Results.pdf
└── templates/                  # Templates for test cases and reports
    ├── template-test-case.md
    ├── template-test-report.md
    └── template-bug-report.md
```

## Test Case Categories

### Authentication (TC-AUTH)
- User registration
- User login
- Wallet authentication
- Password reset
- Email verification
- Session management

### Deposits (TC-DEPOSIT)
- Create deposit
- Deposit approval
- Daily profit calculation
- Max earnings cap (3x)
- Deposit status tracking

### Withdrawals (TC-WITHDRAWAL)
- Withdrawal request
- Withdrawal processing
- Balance deduction
- Withdrawal status
- Failed withdrawals

### Profile (TC-PROFILE)
- Profile data display
- Balance calculation
- Investment tracking
- Rank system
- Token holdings

### Referrals (TC-REFERRAL)
- Referral code generation
- Referral tracking
- Referral bonuses
- Downline visualization

### Generations (TC-GENERATION)
- Generation commission calculation
- 15-level deep commission tracking
- Daily generation profit (0.10%)
- Generation earnings display

## Test Execution Guidelines

### Manual Testing
1. Review test case document
2. Execute test steps as documented
3. Record actual results
4. Capture screenshots for evidence
5. Document any discrepancies
6. Report bugs using bug template

### Automated Testing
1. Ensure test environment is ready
2. Run test suite: `npm run test`
3. Review test results
4. Check Cypress dashboard for screenshots/videos
5. Update test scripts if needed
6. Generate PDF report

## Test Data

Test accounts for manual testing:
- Test User 1: `testuser01` / `password123`
- Test User 2: `testuser02` / `password123`
- Admin Account: `admin@kubexchain.com` / `admin123`

Test wallet addresses:
- Wallet 1: `0x742d35Cc6634C0532925a3b844Bc9e7595f8fE45`
- Wallet 2: `0x8626f6940E2eb28930eFb4CeF49B2d1F2c9C1199`

## Environment Information

- **Production URL:** https://kubexchain.com
- **Staging URL:** https://staging.kubexchain.com
- **Backend API:** https://api.kubexchain.com
- **Database:** MongoDB Atlas

## Reporting Issues

1. Use the bug report template in `/templates`
2. Include steps to reproduce
3. Attach screenshots/videos
4. Note browser and device information
5. Assign severity and priority

## Version History

| Version | Date | Description | Author |
|---------|------|-------------|--------|
| 1.0 | 2026-01-20 | Initial testing structure | Development Team |

---

For questions or issues, contact: development@kubexchain.com
