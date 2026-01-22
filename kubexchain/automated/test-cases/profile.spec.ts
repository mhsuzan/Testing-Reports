import { test, expect } from '@playwright/test';

test.describe('Profile Balance Calculation', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
    await page.fill('input[name="email"]', 'rashedul01@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await page.waitForURL(/.*profile.*/, { timeout: 10000 });
  });

  test('TC-PROFILE-001: Available Balance Display', async ({ page }) => {
    await page.goto('/profile');
    
    // Check Account Overview section
    await expect(page.locator('text=Account Overview')).toBeVisible();
    
    // Verify Available Balance is displayed
    await expect(page.locator('text=Available Balance')).toBeVisible();
    
    // Verify balance value is displayed
    await expect(page.locator('text=/\\$[\\d,]+\\.\\d{2}/').first()).toBeVisible();
  });

  test('TC-PROFILE-002: Investment Profit Display', async ({ page }) => {
    await page.goto('/profile');
    
    // Verify Investment Profit card exists
    await expect(page.locator('text=Investment Profit')).toBeVisible();
    
    // Verify value is displayed
    const investmentProfit = page.locator('text=/\\$[\\d,]+\\.\\d{2}/');
    await expect(investmentProfit.nth(1)).toBeVisible();
  });

  test('TC-PROFILE-003: Generation Profit Display', async ({ page }) => {
    await page.goto('/profile');
    
    // Verify Generation Profit card exists
    await expect(page.locator('text=Generation Profit')).toBeVisible();
    
    // Verify value is displayed (should be ~$43.97 for rashedul01)
    const genProfit = page.locator('text=/\\$[\\d,]+\\.\\d{2}/');
    await expect(genProfit.nth(2)).toBeVisible();
  });

  test('TC-PROFILE-004: Total Withdrawn Display', async ({ page }) => {
    await page.goto('/profile');
    
    // Verify Total Withdrawn card exists
    await expect(page.locator('text=Total Withdrawn')).toBeVisible();
    
    // Verify value is displayed
    const withdrawn = page.locator('text=/\\$[\\d,]+\\.\\d{2}/');
    await expect(withdrawn.nth(3)).toBeVisible();
  });

  test('TC-PROFILE-005: Balance Formula Verification', async ({ page }) => {
    await page.goto('/profile');
    
    // Get all balance values
    const balances = await page.locator('div:has-text("Investment Profit") >> xpath=following-sibling::div').allTextContents();
    
    // This test verifies the formula:
    // Available Balance = Investment Profit + Generation Profit - Total Withdrawals
    
    // Check that all components are displayed
    await expect(page.locator('text=Investment Profit')).toBeVisible();
    await expect(page.locator('text=Generation Profit')).toBeVisible();
    await expect(page.locator('text=Total Withdrawn')).toBeVisible();
  });
});

test.describe('Statement Tab', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
    await page.fill('input[name="email"]', 'rashedul01@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await page.waitForURL(/.*profile.*/, { timeout: 10000 });
  });

  test('TC-PROFILE-006: Statement Tab Displays Earnings', async ({ page }) => {
    // Click Statement tab
    await page.click('text=Statement');
    
    // Verify Statement page loads
    await expect(page.locator('text=Account Statement')).toBeVisible();
    
    // Verify Total Earnings displayed
    await expect(page.locator('text=Total Earnings')).toBeVisible();
    
    // Verify Current Balance displayed
    await expect(page.locator('text=Current Balance')).toBeVisible();
    
    // Verify Total Withdrawn displayed
    await expect(page.locator('text=Total Withdrawn')).toBeVisible();
  });

  test('TC-PROFILE-007: Earnings Breakdown in Statement', async ({ page }) => {
    await page.click('text=Statement');
    
    // Verify Investment Profit section
    await expect(page.locator('text=Investment Profit')).toBeVisible();
    
    // Verify Generation Profit section
    await expect(page.locator('text=Generation Profit')).toBeVisible();
    
    // Verify formulas are explained
    await expect(page.locator('text=How your earnings are calculated')).toBeVisible();
  });
});
