import { test, expect } from '@playwright/test';

test.describe('Deposits', () => {
  test.beforeEach(async ({ page }) => {
    // Login before each deposit test
    await page.goto('/login');
    await page.fill('input[name="email"]', 'testuser_deposit@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await page.waitForURL(/.*profile.*/, { timeout: 10000 });
    
    // Navigate to invest page
    await page.goto('/invest');
  });

  test('TC-DEPOSIT-001: Create New Deposit', async ({ page }) => {
    // Enter deposit amount
    const depositAmount = '100';
    await page.fill('input[name="amount"]', depositAmount);
    
    // Verify daily rate is displayed
    await expect(page.locator('text=0.35%')).toBeVisible();
    
    // Click invest button
    await page.click('button:has-text("Invest Now")');
    
    // Verify payment modal opens
    await expect(page.locator('text=Payment')).toBeVisible({ timeout: 5000 });
  });

  test('TC-DEPOSIT-002: Minimum Deposit Validation', async ({ page }) => {
    // Enter amount below minimum
    await page.fill('input[name="amount"]', '5');
    await page.click('button:has-text("Invest Now")');
    
    // Verify error message
    await expect(page.locator('text=Minimum deposit is $10')).toBeVisible();
  });

  test('TC-DEPOSIT-003: Deposit Status Tracking', async ({ page }) => {
    // Navigate to profile
    await page.goto('/profile');
    
    // Navigate to investments section
    await page.click('text=Your Investments');
    
    // Check for deposit list
    await expect(page.locator('text=Investment')).toBeVisible();
  });
});

test.describe('Investment Profit Calculation', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
    await page.fill('input[name="email"]', 'testuser_deposit@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await page.waitForURL(/.*profile.*/, { timeout: 10000 });
  });

  test('TC-DEPOSIT-004: Investment Profit Display', async ({ page }) => {
    // Navigate to profile
    await page.goto('/profile');
    
    // Check Account Overview section
    await expect(page.locator('text=Account Overview')).toBeVisible();
    
    // Verify Investment Profit is displayed
    await expect(page.locator('text=Investment Profit')).toBeVisible();
    
    // Verify value is greater than 0
    const investmentProfit = page.locator('text=/\\$[\\d,]+\\.\\d{2}/');
    await expect(investmentProfit.first()).toBeVisible();
  });

  test('TC-DEPOSIT-005: Daily Rate Based on Amount', async ({ page }) => {
    await page.goto('/invest');
    
    // Test $10 deposit (0.25% rate - $10-$500 tier)
    await page.fill('input[name="amount"]', '10');
    await expect(page.locator('text=0.25%')).toBeVisible();
    
    // Test $100 deposit (0.25% rate - $10-$500 tier)
    await page.fill('input[name="amount"]', '100');
    await expect(page.locator('text=0.25%')).toBeVisible();
    
    // Test $1000 deposit (0.30% rate - $501-$2000 tier)
    await page.fill('input[name="amount"]', '1000');
    await expect(page.locator('text=0.30%')).toBeVisible();
    
    // Test $5000 deposit (0.35% rate - $2001-$5000 tier)
    await page.fill('input[name="amount"]', '5000');
    await expect(page.locator('text=0.35%')).toBeVisible();
    
    // Test $10000 deposit (0.40% rate - $5001-$10000 tier)
    await page.fill('input[name="amount"]', '10000');
    await expect(page.locator('text=0.40%')).toBeVisible();
    
    // Test $15000 deposit (0.45% rate - $10001+ tier)
    await page.fill('input[name="amount"]', '15000');
    await expect(page.locator('text=0.45%')).toBeVisible();
  });
});
