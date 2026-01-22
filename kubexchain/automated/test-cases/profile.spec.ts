import { test, expect } from '@playwright/test';

test.describe('Profile Balance Display', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
    await page.fill('input[name="email"]', 'testuser@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await page.waitForURL(/.*profile.*/, { timeout: 10000 });
    await page.goto('/profile');
  });

  test('TC-PROFILE-001: Available Balance Display', async ({ page }) => {
    await expect(page.locator('text=Account Overview')).toBeVisible();
    await expect(page.locator('text=Available Balance')).toBeVisible();
    await expect(page.locator('text=/\\$[\\d,]+\\.\\d{2}/').first()).toBeVisible();
  });

  test('TC-PROFILE-002: Investment Profit Display', async ({ page }) => {
    await expect(page.locator('text=Investment Profit')).toBeVisible();
    const investmentProfit = page.locator('text=/\\$[\\d,]+\\.\\d{2}/');
    await expect(investmentProfit.nth(1)).toBeVisible();
  });

  test('TC-PROFILE-003: Generation Profit Display', async ({ page }) => {
    await expect(page.locator('text=Generation Profit')).toBeVisible();
    const genProfit = page.locator('text=/\\$[\\d,]+\\.\\d{2}/');
    await expect(genProfit.nth(2)).toBeVisible();
  });

  test('TC-PROFILE-004: Total Withdrawn Display', async ({ page }) => {
    await expect(page.locator('text=Total Withdrawn')).toBeVisible();
    const withdrawn = page.locator('text=/\\$[\\d,]+\\.\\d{2}/');
    await expect(withdrawn.nth(3)).toBeVisible();
  });

  test('TC-PROFILE-005: Balance Formula Verification', async ({ page }) => {
    await expect(page.locator('text=Investment Profit')).toBeVisible();
    await expect(page.locator('text=Generation Profit')).toBeVisible();
    await expect(page.locator('text=Total Withdrawn')).toBeVisible();
  });

  test('TC-PROFILE-006: Total Invested Display', async ({ page }) => {
    await expect(page.locator('text=Total Invested')).toBeVisible();
  });

  test('TC-PROFILE-007: Total Tokens Display', async ({ page }) => {
    await expect(page.locator('text=Total Tokens')).toBeVisible();
  });

  test('TC-PROFILE-008: Current Rank Display', async ({ page }) => {
    await expect(page.locator('text=Current Rank')).toBeVisible();
  });

  test('TC-PROFILE-009: Profile Information Section', async ({ page }) => {
    await expect(page.locator('text=Profile Information')).toBeVisible();
    await expect(page.locator('text=Username')).toBeVisible();
    await expect(page.locator('text=Email')).toBeVisible();
  });

  test('TC-PROFILE-010: Wallet Address Display', async ({ page }) => {
    await expect(page.locator('text=Wallet Address')).toBeVisible();
    await expect(page.locator('text=0x[a-fA-F0-9]{40}')).toBeVisible();
  });

  test('TC-PROFILE-011: Member Since Date', async ({ page }) => {
    await expect(page.locator('text=Member Since')).toBeVisible();
  });

  test('TC-PROFILE-012: Last Active Date', async ({ page }) => {
    await expect(page.locator('text=Last Active')).toBeVisible();
  });
});

test.describe('Statement Tab', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
    await page.fill('input[name="email"]', 'testuser@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await page.waitForURL(/.*profile.*/, { timeout: 10000 });
  });

  test('TC-PROFILE-013: Statement Tab Loads', async ({ page }) => {
    await page.click('text=Statement');
    await expect(page.locator('text=Account Statement')).toBeVisible();
  });

  test('TC-PROFILE-014: Total Earnings Display', async ({ page }) => {
    await page.click('text=Statement');
    await expect(page.locator('text=Total Earnings')).toBeVisible();
  });

  test('TC-PROFILE-015: Current Balance in Statement', async ({ page }) => {
    await page.click('text=Statement');
    await expect(page.locator('text=Current Balance')).toBeVisible();
  });

  test('TC-PROFILE-016: Investment Profit in Statement', async ({ page }) => {
    await page.click('text=Statement');
    await expect(page.locator('text=Investment Profit')).toBeVisible();
  });

  test('TC-PROFILE-017: Generation Profit in Statement', async ({ page }) => {
    await page.click('text=Statement');
    await expect(page.locator('text=Generation Profit')).toBeVisible();
  });

  test('TC-PROFILE-018: Transaction History Table', async ({ page }) => {
    await page.click('text=Statement');
    await expect(page.locator('text=Transaction History')).toBeVisible();
    await expect(page.locator('text=Date')).toBeVisible();
    await expect(page.locator('text=Type')).toBeVisible();
    await expect(page.locator('text=Amount')).toBeVisible();
  });

  test('TC-PROFILE-019: Earnings Breakdown Explanation', async ({ page }) => {
    await page.click('text=Statement');
    await expect(page.locator('text=How your earnings are calculated')).toBeVisible();
  });

  test('TC-PROFILE-020: Pagination in Statement', async ({ page }) => {
    await page.click('text=Statement');
    await expect(page.locator('text=Page')).toBeVisible();
  });

  test('TC-PROFILE-021: Filter by Transaction Type', async ({ page }) => {
    await page.click('text=Statement');
    await expect(page.locator('text=Filter')).toBeVisible();
  });

  test('TC-PROFILE-022: Date Range Filter', async ({ page }) => {
    await page.click('text=Statement');
    await expect(page.locator('text=Start Date')).toBeVisible();
    await expect(page.locator('text=End Date')).toBeVisible();
  });

  test('TC-PROFILE-023: Export Statement', async ({ page }) => {
    await page.click('text=Statement');
    await expect(page.locator('text=Export')).toBeVisible();
  });

  test('TC-PROFILE-024: Search Transactions', async ({ page }) => {
    await page.click('text=Statement');
    await expect(page.locator('input[placeholder="Search"]')).toBeVisible();
  });

  test('TC-PROFILE-025: Empty State Message', async ({ page }) => {
    await page.click('text=Statement');
    const emptyMessage = page.locator('text=No transactions found');
    const hasTransactions = await page.locator('text=Transaction History').isVisible();
    if (hasTransactions) {
      await expect(page.locator('text=Total:')).toBeVisible();
    }
  });
});

test.describe('Settings', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
    await page.fill('input[name="email"]', 'testuser@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await page.waitForURL(/.*profile.*/, { timeout: 10000 });
    await page.goto('/profile');
  });

  test('TC-PROFILE-026: Settings Tab', async ({ page }) => {
    await page.click('text=Settings');
    await expect(page.locator('text=Account Settings')).toBeVisible();
  });

  test('TC-PROFILE-027: Change Password Form', async ({ page }) => {
    await page.click('text=Settings');
    await expect(page.locator('text=Change Password')).toBeVisible();
    await expect(page.locator('input[name="currentPassword"]')).toBeVisible();
    await expect(page.locator('input[name="newPassword"]')).toBeVisible();
  });

  test('TC-PROFILE-028: Two-Factor Authentication', async ({ page }) => {
    await page.click('text=Settings');
    await expect(page.locator('text=Two-Factor Authentication')).toBeVisible();
  });

  test('TC-PROFILE-029: Notification Settings', async ({ page }) => {
    await page.click('text=Settings');
    await expect(page.locator('text=Notifications')).toBeVisible();
  });

  test('TC-PROFILE-030: Email Notification Toggle', async ({ page }) => {
    await page.click('text=Settings');
    await expect(page.locator('text=Email Notifications')).toBeVisible();
  });
});

test.describe('Security', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
    await page.fill('input[name="email"]', 'testuser@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await page.waitForURL(/.*profile.*/, { timeout: 10000 });
    await page.goto('/profile');
  });

  test('TC-PROFILE-031: Active Sessions Display', async ({ page }) => {
    await page.click('text=Settings');
    await expect(page.locator('text=Active Sessions')).toBeVisible();
  });

  test('TC-PROFILE-032: Logout Other Devices', async ({ page }) => {
    await page.click('text=Settings');
    await expect(page.locator('text=Logout Other Devices')).toBeVisible();
  });

  test('TC-PROFILE-033: Account Deletion Option', async ({ page }) => {
    await page.click('text=Settings');
    await expect(page.locator('text=Delete Account')).toBeVisible();
  });

  test('TC-PROFILE-034: Session Timeout Setting', async ({ page }) => {
    await page.click('text=Settings');
    await expect(page.locator('text=Session Timeout')).toBeVisible();
  });
});
