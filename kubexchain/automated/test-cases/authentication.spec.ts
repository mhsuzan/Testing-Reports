import { test, expect } from '@playwright/test';

test.describe('Authentication', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
  });

  test('TC-AUTH-001: User Login with Email/Password', async ({ page }) => {
    // Enter valid credentials
    await page.fill('input[name="email"]', 'testuser@kubexchain.test');
    await page.fill('input[name="password"]', 'Test@123456');
    
    // Submit form
    await page.click('button[type="submit"]');
    
    // Verify redirect to dashboard
    await expect(page).toHaveURL(/.*profile.*/, { timeout: 10000 });
    
    // Verify user is logged in
    await expect(page.locator('text=Welcome back')).toBeVisible({ timeout: 5000 });
  });

  test('TC-AUTH-002: Invalid Login Shows Error', async ({ page }) => {
    // Enter invalid credentials
    await page.fill('input[name="email"]', 'invalid@test.com');
    await page.fill('input[name="password"]', 'wrongpassword');
    
    // Submit form
    await page.click('button[type="submit"]');
    
    // Verify error message
    await expect(page.locator('text=Invalid email or password')).toBeVisible({ timeout: 5000 });
  });

  test('TC-AUTH-003: Login Form Validation', async ({ page }) => {
    // Leave fields empty
    await page.click('button[type="submit"]');
    
    // Verify required field errors
    await expect(page.locator('text=Please provide email and password')).toBeVisible();
  });
});

test.describe('Registration', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/register');
  });

  test('TC-AUTH-004: User Registration', async ({ page }) => {
    const testUser = `test_${Date.now()}@kubexchain.test`;
    
    // Fill registration form
    await page.fill('input[name="username"]', `testuser_${Date.now()}`);
    await page.fill('input[name="email"]', testUser);
    await page.fill('input[name="password"]', 'Test@123456');
    await page.fill('input[name="confirmPassword"]', 'Test@123456');
    
    // Submit form
    await page.click('button[type="submit"]');
    
    // Verify success message
    await expect(page.locator('text=Registration successful')).toBeVisible({ timeout: 10000 });
  });

  test('TC-AUTH-005: Password Mismatch Shows Error', async ({ page }) => {
    await page.fill('input[name="username"]', 'testuser');
    await page.fill('input[name="email"]', 'test@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.fill('input[name="confirmPassword"]', 'Different@123');
    
    await page.click('button[type="submit"]');
    
    await expect(page.locator('text=Passwords do not match')).toBeVisible();
  });
});
