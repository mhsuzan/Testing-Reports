import { test, expect } from '@playwright/test';

test.describe('Deposits', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/invest');
  });

  test('TC-DEPOSIT-001: Invest Page Loads', async ({ page }) => {
    await expect(page).toHaveURL(/.*invest.*/);
    await expect(page.locator('h1, h2')).toContainText(/Invest|Make Deposit/i);
  });

  test('TC-DEPOSIT-002: Deposit Form Present', async ({ page }) => {
    await expect(page.locator('input[name="amount"]')).toBeVisible();
    await expect(page.locator('button:has-text("Invest")')).toBeVisible();
  });

  test('TC-DEPOSIT-003: Minimum Deposit Amount Validation', async ({ page }) => {
    await page.fill('input[name="amount"]', '5');
    await page.click('button:has-text("Invest")');
    await expect(page.locator('text=Minimum deposit is $10')).toBeVisible();
  });

  test('TC-DEPOSIT-004: Maximum Deposit Amount Validation', async ({ page }) => {
    await page.fill('input[name="amount"]', '100000');
    await page.click('button:has-text("Invest")');
    await expect(page.locator('text=Maximum deposit is $50,000')).toBeVisible();
  });

  test('TC-DEPOSIT-005: Valid Deposit Amount', async ({ page }) => {
    await page.fill('input[name="amount"]', '100');
    await page.click('button:has-text("Invest")');
    await expect(page.locator('text=Payment gateway opening')).toBeVisible({ timeout: 5000 });
  });

  test('TC-DEPOSIT-006: Daily Rate Display for $10 (0.25%)', async ({ page }) => {
    await page.fill('input[name="amount"]', '10');
    await expect(page.locator('text=0.25%')).toBeVisible();
  });

  test('TC-DEPOSIT-007: Daily Rate Display for $100 (0.25%)', async ({ page }) => {
    await page.fill('input[name="amount"]', '100');
    await expect(page.locator('text=0.25%')).toBeVisible();
  });

  test('TC-DEPOSIT-008: Daily Rate Display for $1000 (0.30%)', async ({ page }) => {
    await page.fill('input[name="amount"]', '1000');
    await expect(page.locator('text=0.30%')).toBeVisible();
  });

  test('TC-DEPOSIT-009: Daily Rate Display for $2000 (0.30%)', async ({ page }) => {
    await page.fill('input[name="amount"]', '2000');
    await expect(page.locator('text=0.30%')).toBeVisible();
  });

  test('TC-DEPOSIT-010: Daily Rate Display for $3000 (0.35%)', async ({ page }) => {
    await page.fill('input[name="amount"]', '3000');
    await expect(page.locator('text=0.35%')).toBeVisible();
  });

  test('TC-DEPOSIT-011: Daily Rate Display for $5000 (0.35%)', async ({ page }) => {
    await page.fill('input[name="amount"]', '5000');
    await expect(page.locator('text=0.35%')).toBeVisible();
  });

  test('TC-DEPOSIT-012: Daily Rate Display for $7500 (0.40%)', async ({ page }) => {
    await page.fill('input[name="amount"]', '7500');
    await expect(page.locator('text=0.40%')).toBeVisible();
  });

  test('TC-DEPOSIT-013: Daily Rate Display for $10000 (0.40%)', async ({ page }) => {
    await page.fill('input[name="amount"]', '10000');
    await expect(page.locator('text=0.40%')).toBeVisible();
  });

  test('TC-DEPOSIT-014: Daily Rate Display for $15000 (0.45%)', async ({ page }) => {
    await page.fill('input[name="amount"]', '15000');
    await expect(page.locator('text=0.45%')).toBeVisible();
  });

  test('TC-DEPOSIT-015: Daily Profit Calculation Display', async ({ page }) => {
    await page.fill('input[name="amount"]', '1000');
    await expect(page.locator('text=Daily Profit')).toBeVisible();
    await expect(page.locator('text=$3.00')).toBeVisible();
  });

  test('TC-DEPOSIT-016: Max Earnings Display (3x)', async ({ page }) => {
    await page.fill('input[name="amount"]', '1000');
    await expect(page.locator('text=Max Earnings')).toBeVisible();
    await expect(page.locator('text=$3,000.00')).toBeVisible();
  });

  test('TC-DEPOSIT-017: Multiple Deposit Tiers', async ({ page }) => {
    await page.fill('input[name="amount"]', '10000');
    await expect(page.locator('text=0.40%')).toBeVisible();
    await expect(page.locator('text=$40.00')).toBeVisible();
    await expect(page.locator('text=$30,000.00')).toBeVisible();
  });

  test('TC-DEPOSIT-018: Deposit Currency Selection', async ({ page }) => {
    await expect(page.locator('select[name="currency"]')).toBeVisible();
    await page.selectOption('select[name="currency"]', 'USDT');
  });

  test('TC-DEPOSIT-019: Deposit Network Selection', async ({ page }) => {
    await expect(page.locator('select[name="network"]')).toBeVisible();
    await page.selectOption('select[name="network"]', 'TRC20');
  });

  test('TC-DEPOSIT-020: Payment Gateway Opens', async ({ page }) => {
    await page.fill('input[name="amount"]', '100');
    await page.click('button:has-text("Invest Now")');
    await expect(page.locator('iframe[title="Payment Gateway"]')).toBeVisible({ timeout: 10000 });
  });

  test('TC-DEPOSIT-021: Deposit Success Page', async ({ page }) => {
    await page.goto('/investment/success?id=test123');
    await expect(page.locator('text=Deposit Successful')).toBeVisible();
  });

  test('TC-DEPOSIT-022: Deposit Cancel Page', async ({ page }) => {
    await page.goto('/investment/cancel?id=test123');
    await expect(page.locator('text=Deposit Cancelled')).toBeVisible();
  });

  test('TC-DEPOSIT-023: Empty Amount Field', async ({ page }) => {
    await page.click('button:has-text("Invest")');
    await expect(page.locator('text=Please enter an amount')).toBeVisible();
  });

  test('TC-DEPOSIT-024: Decimal Amount Validation', async ({ page }) => {
    await page.fill('input[name="amount"]', '100.50');
    await expect(page.locator('text=Valid amount')).toBeVisible();
  });

  test('TC-DEPOSIT-025: Non-numeric Input Blocked', async ({ page }) => {
    await page.fill('input[name="amount"]', 'abc');
    await expect(page.locator('text=Please enter a valid number')).toBeVisible();
  });
});

test.describe('Investment Dashboard', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/profile');
  });

  test('TC-DEPOSIT-026: Active Investments Display', async ({ page }) => {
    await expect(page.locator('text=Active Investments')).toBeVisible();
  });

  test('TC-DEPOSIT-027: Investment Details Show Amount', async ({ page }) => {
    await expect(page.locator('text=Investment Amount')).toBeVisible();
  });

  test('TC-DEPOSIT-028: Investment Details Show Daily Rate', async ({ page }) => {
    await expect(page.locator('text=Daily Rate')).toBeVisible();
  });

  test('TC-DEPOSIT-029: Investment Details Show Total Earned', async ({ page }) => {
    await expect(page.locator('text=Total Earned')).toBeVisible();
  });

  test('TC-DEPOSIT-030: Investment Details Show Days Active', async ({ page }) => {
    await expect(page.locator('text=Days Active')).toBeVisible();
  });

  test('TC-DEPOSIT-031: Investment Progress Bar', async ({ page }) => {
    await expect(page.locator('progress, [role="progressbar"]')).toBeVisible();
  });

  test('TC-DEPOSIT-032: Max Earnings Progress', async ({ page }) => {
    await expect(page.locator('text=Progress to Max')).toBeVisible();
  });

  test('TC-DEPOSIT-033: Completed Investments Section', async ({ page }) => {
    await expect(page.locator('text=Completed')).toBeVisible();
  });

  test('TC-DEPOSIT-034: Pending Investments Section', async ({ page }) => {
    await expect(page.locator('text=Pending')).toBeVisible();
  });

  test('TC-DEPOSIT-035: Investment List Pagination', async ({ page }) => {
    await expect(page.locator('text=Page')).toBeVisible();
  });
});
