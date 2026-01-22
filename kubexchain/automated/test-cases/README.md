# Automated Test Scripts

This folder contains automated test scripts for the KubexChain project.

## Testing Framework

- **Framework:** Playwright
- **Language:** TypeScript
- **Reporting:** Allure Reports

## Installation

```bash
npm install -D @playwright/test
npx playwright install
```

## Running Tests

```bash
# Run all tests
npm run test

# Run specific test file
npm run test -- tests/authentication.spec.ts

# Run with UI
npm run test:ui

# Run with headed browser
npm run test -- --headed

# Run specific test
npm run test -- -g "login"
```

## Test Configuration

See `playwright.config.ts` for configuration options.

## Writing Tests

See individual test files for examples.
