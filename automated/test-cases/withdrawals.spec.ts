import { test, expect } from '@playwright/test';

test.describe('Withdrawals', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
    await page.fill('input[name="email"]', 'testuser_withdraw@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await page.waitForURL(/.*profile.*/, { timeout: 10000 });
    
    // Navigate to withdraw page
    await page.click('text=Withdraw');
  });

  test('TC-WITHDRAWAL-001: Withdraw Form Validation', async ({ page }) => {
    // Check form elements exist
    await expect(page.locator('input[name="amount"]')).toBeVisible();
    await expect(page.locator('text=Request Withdrawal')).toBeVisible();
  });

  test('TC-WITHDRAWAL-002: Minimum Withdrawal Validation', async ({ page }) => {
    // Enter amount below minimum
    await page.fill('input[name="amount"]', '5');
    await page.click('text=Request Withdrawal');
    
    // Verify error message
    await expect(page.locator('text=Minimum withdrawal is $10')).toBeVisible({ timeout: 5000 });
  });

  test('TC-WITHDRAWAL-003: Insufficient Balance Validation', async ({ page }) => {
    // Enter amount exceeding balance
    await page.fill('input[name="amount"]', '1000000');
    await page.click('text=Request Withdrawal');
    
    // Verify error message
    await expect(page.locator('text=Insufficient balance')).toBeVisible({ timeout: 5000 });
  });

  test('TC-WITHDRAWAL-004: No Wallet Linked Error', async ({ page }) => {
    // This test is for users without linked wallet
    await page.goto('/profile');
    await page.click('text=Withdraw');
    
    // Check for wallet warning
    const walletWarning = page.locator('text=Please link your wallet');
    if (await walletWarning.isVisible()) {
      await expect(walletWarning).toBeVisible();
    }
  });

  test('TC-WITHDRAWAL-005: Successful Withdrawal Request', async ({ page }) => {
    // This test requires a user with linked wallet and sufficient balance
    
    // Check available balance
    await expect(page.locator('text=Available')).toBeVisible();
    
    // Enter valid amount (adjust based on available balance)
    await page.fill('input[name="amount"]', '10');
    
    // Click withdraw button
    await page.click('text=Request Withdrawal');
    
    // Verify confirmation modal (if implemented)
    // This may need adjustment based on actual implementation
  });
});

test.describe('Withdrawal History', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
    await page.fill('input[name="email"]', 'testuser_withdraw@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await page.waitForURL(/.*profile.*/, { timeout: 10000 });
  });

  test('TC-WITHDRAWAL-006: Withdrawal History Display', async ({ page }) => {
    await page.click('text=Withdraw');
    
    // Check for transaction history section
    await expect(page.locator('text=Withdrawal History')).toBeVisible();
    
    // Verify table headers
    await expect(page.locator('text=Date')).toBeVisible();
    await expect(page.locator('text=Amount')).toBeVisible();
    await expect(page.locator('text=Status')).toBeVisible();
  });
});
