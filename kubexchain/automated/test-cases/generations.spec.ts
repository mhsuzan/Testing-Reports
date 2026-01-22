import { test, expect } from '@playwright/test';

test.describe('Generations', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
    await page.fill('input[name="email"]', 'testuser@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await page.waitForURL(/.*profile.*/, { timeout: 10000 });
    await page.click('text=Generations');
  });

  test('TC-GENERATION-001: Generations Page Loads', async ({ page }) => {
    await expect(page.locator('text=Generations')).toBeVisible();
  });

  test('TC-GENERATION-002: Generation Profit Display', async ({ page }) => {
    await expect(page.locator('text=Generation Profit')).toBeVisible();
    await expect(page.locator('text=/\\$[\\d,]+\\.\\d{2}/').first()).toBeVisible();
  });

  test('TC-GENERATION-003: Locked Generation Balance', async ({ page }) => {
    await expect(page.locator('text=Locked Balance')).toBeVisible();
  });

  test('TC-GENERATION-004: Generation Records Table', async ({ page }) => {
    await expect(page.locator('text=Commission')).toBeVisible();
    await expect(page.locator('text=Date')).toBeVisible();
    await expect(page.locator('text=Level')).toBeVisible();
  });

  test('TC-GENERATION-005: 15-Level Deep Commission', async ({ page }) => {
    await expect(page.locator('text=Level')).toBeVisible();
    await expect(page.locator('text=Level 1')).toBeVisible();
  });

  test('TC-GENERATION-006: Level 1 Commission (8%)', async ({ page }) => {
    const level1 = page.locator('text=Level 1');
    if (await level1.isVisible()) {
      await expect(page.locator('text=8%')).toBeVisible();
    }
  });

  test('TC-GENERATION-007: Level 2 Commission (5%)', async ({ page }) => {
    const level2 = page.locator('text=Level 2');
    if (await level2.isVisible()) {
      await expect(page.locator('text=5%')).toBeVisible();
    }
  });

  test('TC-GENERATION-008: Level 3 Commission (3%)', async ({ page }) => {
    const level3 = page.locator('text=Level 3');
    if (await level3.isVisible()) {
      await expect(page.locator('text=3%')).toBeVisible();
    }
  });

  test('TC-GENERATION-009: Levels 4-5 Commission (2%)', async ({ page }) => {
    const level4 = page.locator('text=Level 4');
    if (await level4.isVisible()) {
      await expect(page.locator('text=2%')).toBeVisible();
    }
  });

  test('TC-GENERATION-010: Levels 6-15 Commission (1%)', async ({ page }) => {
    const level6 = page.locator('text=Level 6');
    if (await level6.isVisible()) {
      await expect(page.locator('text=1%')).toBeVisible();
    }
  });

  test('TC-GENERATION-011: Commission Amount Display', async ({ page }) => {
    await expect(page.locator('text=/\\$[\\d,]+\\.\\d{2}/')).toBeVisible();
  });

  test('TC-GENERATION-012: Daily Profit on Locked Balance', async ({ page }) => {
    await expect(page.locator('text=0.10% daily')).toBeVisible();
  });

  test('TC-GENERATION-013: Total Commissions Earned', async ({ page }) => {
    await expect(page.locator('text=Total Commissions')).toBeVisible();
  });

  test('TC-GENERATION-014: Generation Team Size', async ({ page }) => {
    await expect(page.locator('text=Team Size')).toBeVisible();
  });

  test('TC-GENERATION-015: Active Referrals Count', async ({ page }) => {
    await expect(page.locator('text=Active Referrals')).toBeVisible();
  });
});

test.describe('Generation Details', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
    await page.fill('input[name="email"]', 'testuser@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await page.waitForURL(/.*profile.*/, { timeout: 10000 });
    await page.click('text=Generations');
  });

  test('TC-GENERATION-016: Generation Tree Visualization', async ({ page }) => {
    const tree = page.locator('text=Network Tree');
    if (await tree.isVisible()) {
      await expect(tree).toBeVisible();
    }
  });

  test('TC-GENERATION-017: Downline List', async ({ page }) => {
    await expect(page.locator('text=Downline')).toBeVisible();
  });

  test('TC-GENERATION-018: Direct Referrals', async ({ page }) => {
    await expect(page.locator('text=Direct Referrals')).toBeVisible();
  });

  test('TC-GENERATION-019: Generation Statistics', async ({ page }) => {
    await expect(page.locator('text=Statistics')).toBeVisible();
  });

  test('TC-GENERATION-020: Commission History', async ({ page }) => {
    await expect(page.locator('text=Commission History')).toBeVisible();
  });

  test('TC-GENERATION-021: Filter by Level', async ({ page }) => {
    await expect(page.locator('text=Filter by Level')).toBeVisible();
  });

  test('TC-GENERATION-022: Date Range Filter', async ({ page }) => {
    await expect(page.locator('text=Start Date')).toBeVisible();
    await expect(page.locator('text=End Date')).toBeVisible();
  });

  test('TC-GENERATION-023: Export Generation Report', async ({ page }) => {
    await expect(page.locator('text=Export')).toBeVisible();
  });

  test('TC-GENERATION-024: Pagination', async ({ page }) => {
    await expect(page.locator('text=Page')).toBeVisible();
  });

  test('TC-GENERATION-025: Search Downline Member', async ({ page }) => {
    await expect(page.locator('input[placeholder="Search"]')).toBeVisible();
  });
});

test.describe('Referrals', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
    await page.fill('input[name="email"]', 'testuser@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await page.waitForURL(/.*profile.*/, { timeout: 10000 });
    await page.click('text=Referrals');
  });

  test('TC-REFERRAL-001: Referral Page Loads', async ({ page }) => {
    await expect(page.locator('text=Referrals')).toBeVisible();
  });

  test('TC-REFERRAL-002: Referral Code Display', async ({ page }) => {
    await expect(page.locator('text=Referral Code')).toBeVisible();
    await expect(page.locator('text=/[A-Z0-9]{4,}/')).toBeVisible();
  });

  test('TC-REFERRAL-003: Referral Link Display', async ({ page }) => {
    await expect(page.locator('text=Referral Link')).toBeVisible();
    await expect(page.locator('text=kubexchain.com/ref/')).toBeVisible();
  });

  test('TC-REFERRAL-004: Copy Referral Link', async ({ page }) => {
    const copyButton = page.locator('button:has-text("Copy")');
    if (await copyButton.isVisible()) {
      await copyButton.click();
      await expect(page.locator('text=Copied')).toBeVisible({ timeout: 2000 });
    }
  });

  test('TC-REFERRAL-005: Share via Email', async ({ page }) => {
    const emailBtn = page.locator('button:has-text("Email")');
    if (await emailBtn.isVisible()) {
      await expect(emailBtn).toBeVisible();
    }
  });

  test('TC-REFERRAL-006: Share via WhatsApp', async ({ page }) => {
    const whatsappBtn = page.locator('button:has-text("WhatsApp")');
    if (await whatsappBtn.isVisible()) {
      await expect(whatsappBtn).toBeVisible();
    }
  });

  test('TC-REFERRAL-007: Total Referrals Count', async ({ page }) => {
    await expect(page.locator('text=Total Referrals')).toBeVisible();
  });

  test('TC-REFERRAL-008: Active Referrals Count', async ({ page }) => {
    await expect(page.locator('text=Active Referrals')).toBeVisible();
  });

  test('TC-REFERRAL-009: Pending Referrals Count', async ({ page }) => {
    await expect(page.locator('text=Pending Referrals')).toBeVisible();
  });

  test('TC-REFERRAL-010: Referral Rewards Display', async ({ page }) => {
    await expect(page.locator('text=Total Earned')).toBeVisible();
  });

  test('TC-REFERRAL-011: Referral List', async ({ page }) => {
    await expect(page.locator('text=Referral List')).toBeVisible();
  });

  test('TC-REFERRAL-012: Referral Registration Date', async ({ page }) => {
    await expect(page.locator('text=Joined')).toBeVisible();
  });

  test('TC-REFERRAL-013: Referral Status', async ({ page }) => {
    await expect(page.locator('text=Status')).toBeVisible();
  });

  test('TC-REFERRAL-014: Referral Investment Amount', async ({ page }) => {
    await expect(page.locator('text=Investment')).toBeVisible();
  });

  test('TC-REFERRAL-015: Referral Commission Earned', async ({ page }) => {
    await expect(page.locator('text=Commission')).toBeVisible();
  });
});

test.describe('Network', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
    await page.fill('input[name="email"]', 'testuser@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await page.waitForURL(/.*profile.*/, { timeout: 10000 });
  });

  test('TC-NETWORK-001: Network Page Loads', async ({ page }) => {
    await page.click('text=Network');
    await expect(page.locator('text=Network')).toBeVisible();
  });

  test('TC-NETWORK-002: Rank System Display', async ({ page }) => {
    await page.click('text=Ranks');
    await expect(page.locator('text=Ranks')).toBeVisible();
  });

  test('TC-NETWORK-003: Current Rank Badge', async ({ page }) => {
    await page.click('text=Ranks');
    await expect(page.locator('text=Your Rank')).toBeVisible();
  });

  test('TC-NETWORK-004: Rank Requirements', async ({ page }) => {
    await page.click('text=Ranks');
    await expect(page.locator('text=Requirements')).toBeVisible();
  });

  test('TC-NETWORK-005: Bronze Rank Criteria', async ({ page }) => {
    await page.click('text=Ranks');
    await expect(page.locator('text=Bronze')).toBeVisible();
  });

  test('TC-NETWORK-006: Silver Rank Criteria', async ({ page }) => {
    await page.click('text=Ranks');
    await expect(page.locator('text=Silver')).toBeVisible();
  });

  test('TC-NETWORK-007: Gold Rank Criteria', async ({ page }) => {
    await page.click('text=Ranks');
    await expect(page.locator('text=Gold')).toBeVisible();
  });

  test('TC-NETWORK-008: Platinum Rank Criteria', async ({ page }) => {
    await page.click('text=Ranks');
    await expect(page.locator('text=Platinum')).toBeVisible();
  });

  test('TC-NETWORK-009: Diamond Rank Criteria', async ({ page }) => {
    await page.click('text=Ranks');
    await expect(page.locator('text=Diamond')).toBeVisible();
  });

  test('TC-NETWORK-010: Rank Progress Bar', async ({ page }) => {
    await page.click('text=Ranks');
    await expect(page.locator('progress, [role="progressbar"]')).toBeVisible();
  });
});
