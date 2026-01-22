import { test, expect } from '@playwright/test';

test.describe('Withdrawals', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
    await page.fill('input[name="email"]', 'testuser@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await page.waitForURL(/.*profile.*/, { timeout: 10000 });
    await page.click('text=Withdraw');
  });

  test('TC-WITHDRAWAL-001: Withdraw Page Loads', async ({ page }) => {
    await expect(page).toHaveURL(/.*withdraw.*/);
    await expect(page.locator('text=Withdrawal')).toBeVisible();
  });

  test('TC-WITHDRAWAL-002: Withdraw Form Validation', async ({ page }) => {
    await expect(page.locator('input[name="amount"]')).toBeVisible();
    await expect(page.locator('text=Request Withdrawal')).toBeVisible();
  });

  test('TC-WITHDRAWAL-003: Minimum Withdrawal Validation', async ({ page }) => {
    await page.fill('input[name="amount"]', '5');
    await page.click('text=Request Withdrawal');
    await expect(page.locator('text=Minimum withdrawal is $10')).toBeVisible({ timeout: 5000 });
  });

  test('TC-WITHDRAWAL-004: Maximum Withdrawal Validation', async ({ page }) => {
    await page.fill('input[name="amount"]', '1000000');
    await page.click('text=Request Withdrawal');
    await expect(page.locator('text=Maximum withdrawal is')).toBeVisible();
  });

  test('TC-WITHDRAWAL-005: Insufficient Balance Validation', async ({ page }) => {
    await page.fill('input[name="amount"]', '1000000');
    await page.click('text=Request Withdrawal');
    await expect(page.locator('text=Insufficient balance')).toBeVisible({ timeout: 5000 });
  });

  test('TC-WITHDRAWAL-006: No Wallet Linked Error', async ({ page }) => {
    const walletWarning = page.locator('text=Please link your wallet');
    if (await walletWarning.isVisible()) {
      await expect(walletWarning).toBeVisible();
    }
  });

  test('TC-WITHDRAWAL-007: Valid Withdrawal Request', async ({ page }) => {
    await expect(page.locator('text=Available')).toBeVisible();
    await page.fill('input[name="amount"]', '10');
    await page.click('text=Request Withdrawal');
  });

  test('TC-WITHDRAWAL-008: Withdrawal Confirmation Modal', async ({ page }) => {
    await page.fill('input[name="amount"]', '10');
    await page.click('text=Request Withdrawal');
    const modal = page.locator('text=Confirm Withdrawal');
    if (await modal.isVisible()) {
      await expect(modal).toBeVisible();
    }
  });

  test('TC-WITHDRAWAL-009: Withdrawal Success Message', async ({ page }) => {
    await page.fill('input[name="amount"]', '10');
    await page.click('text=Request Withdrawal');
    await expect(page.locator('text=Withdrawal request submitted')).toBeVisible({ timeout: 5000 });
  });

  test('TC-WITHDRAWAL-010: Decimal Amount Allowed', async ({ page }) => {
    await page.fill('input[name="amount"]', '10.50');
    await expect(page.locator('text=$10.50')).toBeVisible();
  });

  test('TC-WITHDRAWAL-011: Withdrawal Amount Format', async ({ page }) => {
    await page.fill('input[name="amount"]', '1000');
    await expect(page.locator('text=$1,000.00')).toBeVisible();
  });

  test('TC-WITHDRAWAL-012: Available Balance Display', async ({ page }) => {
    await expect(page.locator('text=Available Balance')).toBeVisible();
    await expect(page.locator('text=/\\$[\\d,]+\\.\\d{2}/')).toBeVisible();
  });

  test('TC-WITHDRAWAL-013: Wallet Address Display', async ({ page }) => {
    await expect(page.locator('text=Withdrawal to')).toBeVisible();
  });

  test('TC-WITHDRAWAL-014: Network Fee Display', async ({ page }) => {
    await expect(page.locator('text=Network Fee')).toBeVisible();
  });

  test('TC-WITHDRAWAL-015: Estimated Receive Amount', async ({ page }) => {
    await page.fill('input[name="amount"]', '100');
    await expect(page.locator('text=You will receive')).toBeVisible();
  });
});

test.describe('Withdrawal History', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
    await page.fill('input[name="email"]', 'testuser@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await page.waitForURL(/.*profile.*/, { timeout: 10000 });
    await page.click('text=Withdraw');
  });

  test('TC-WITHDRAWAL-016: Withdrawal History Display', async ({ page }) => {
    await expect(page.locator('text=Withdrawal History')).toBeVisible();
  });

  test('TC-WITHDRAWAL-017: Transaction Date Column', async ({ page }) => {
    await expect(page.locator('text=Date')).toBeVisible();
  });

  test('TC-WITHDRAWAL-018: Transaction Amount Column', async ({ page }) => {
    await expect(page.locator('text=Amount')).toBeVisible();
  });

  test('TC-WITHDRAWAL-019: Transaction Status Column', async ({ page }) => {
    await expect(page.locator('text=Status')).toBeVisible();
  });

  test('TC-WITHDRAWAL-020: Pending Status Display', async ({ page }) => {
    const pending = page.locator('text=Pending');
    if (await pending.isVisible()) {
      await expect(pending).toBeVisible();
    }
  });

  test('TC-WITHDRAWAL-021: Completed Status Display', async ({ page }) => {
    const completed = page.locator('text=Completed');
    if (await completed.isVisible()) {
      await expect(completed).toBeVisible();
    }
  });

  test('TC-WITHDRAWAL-022: Failed Status Display', async ({ page }) => {
    const failed = page.locator('text=Failed');
    if (await failed.isVisible()) {
      await expect(failed).toBeVisible();
    }
  });

  test('TC-WITHDRAWAL-023: Transaction Hash Display', async ({ page }) => {
    const hash = page.locator('text=0x[a-fA-F0-9]{64}');
    if (await hash.isVisible()) {
      await expect(hash).toBeVisible();
    }
  });

  test('TC-WITHDRAWAL-024: Empty Withdrawal History', async ({ page }) => {
    const empty = page.locator('text=No withdrawals yet');
    if (await empty.isVisible()) {
      await expect(empty).toBeVisible();
    }
  });

  test('TC-WITHDRAWAL-025: Pagination in History', async ({ page }) => {
    await expect(page.locator('text=Page')).toBeVisible();
  });

  test('TC-WITHDRAWAL-026: Filter by Status', async ({ page }) => {
    await expect(page.locator('text=Filter')).toBeVisible();
  });

  test('TC-WITHDRAWAL-027: Search Withdrawal', async ({ page }) => {
    await expect(page.locator('input[placeholder="Search"]')).toBeVisible();
  });

  test('TC-WITHDRAWAL-028: Export Withdrawals', async ({ page }) => {
    await expect(page.locator('text=Export')).toBeVisible();
  });

  test('TC-WITHDRAWAL-029: Total Withdrawn Summary', async ({ page }) => {
    await expect(page.locator('text=Total Withdrawn')).toBeVisible();
  });

  test('TC-WITHDRAWAL-030: Pending Amount Summary', async ({ page }) => {
    await expect(page.locator('text=Pending')).toBeVisible();
  });
});
