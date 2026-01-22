import { test, expect } from '@playwright/test';

test.describe('Authentication', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
  });

  test('TC-AUTH-001: User Login with Email/Password', async ({ page }) => {
    await page.fill('input[name="email"]', 'testuser@kubexchain.test');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await expect(page).toHaveURL(/.*profile.*/, { timeout: 10000 });
    await expect(page.locator('text=Welcome back')).toBeVisible({ timeout: 5000 });
  });

  test('TC-AUTH-002: Invalid Login Shows Error', async ({ page }) => {
    await page.fill('input[name="email"]', 'invalid@test.com');
    await page.fill('input[name="password"]', 'wrongpassword');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Invalid email or password')).toBeVisible({ timeout: 5000 });
  });

  test('TC-AUTH-003: Login Form Validation - Empty Fields', async ({ page }) => {
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Please provide email and password')).toBeVisible();
  });

  test('TC-AUTH-004: Login with Invalid Email Format', async ({ page }) => {
    await page.fill('input[name="email"]', 'notanemail');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Please enter a valid email')).toBeVisible();
  });

  test('TC-AUTH-005: Login with Short Password', async ({ page }) => {
    await page.fill('input[name="email"]', 'test@test.com');
    await page.fill('input[name="password"]', '123');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Password must be at least')).toBeVisible();
  });

  test('TC-AUTH-006: Password Field Masking', async ({ page }) => {
    const passwordField = page.locator('input[name="password"]');
    await expect(passwordField).toHaveAttribute('type', 'password');
  });

  test('TC-AUTH-007: Forgot Password Link Present', async ({ page }) => {
    await expect(page.locator('text=Forgot Password')).toBeVisible();
  });

  test('TC-AUTH-008: Remember Me Checkbox', async ({ page }) => {
    await expect(page.locator('input[name="remember"]')).toBeVisible();
  });

  test('TC-AUTH-009: Login Page Title', async ({ page }) => {
    await expect(page).toHaveTitle(/.*Login.*|.*Sign.*in.*/i);
  });

  test('TC-AUTH-010: Login with Wallet Address', async ({ page }) => {
    await page.click('text=Connect Wallet');
    const walletInput = page.locator('input[name="walletAddress"]');
    await expect(walletInput).toBeVisible();
  });
});

test.describe('Registration', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/register');
  });

  test('TC-AUTH-011: User Registration', async ({ page }) => {
    const testUser = `test_${Date.now()}@kubexchain.test`;
    await page.fill('input[name="username"]', `testuser_${Date.now()}`);
    await page.fill('input[name="email"]', testUser);
    await page.fill('input[name="password"]', 'Test@123456');
    await page.fill('input[name="confirmPassword"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Registration successful')).toBeVisible({ timeout: 10000 });
  });

  test('TC-AUTH-012: Password Mismatch Shows Error', async ({ page }) => {
    await page.fill('input[name="username"]', 'testuser');
    await page.fill('input[name="email"]', 'test@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.fill('input[name="confirmPassword"]', 'Different@123');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Passwords do not match')).toBeVisible();
  });

  test('TC-AUTH-013: Duplicate Email Registration', async ({ page }) => {
    await page.fill('input[name="username"]', 'testuser2');
    await page.fill('input[name="email"]', 'existing@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.fill('input[name="confirmPassword"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Email already registered')).toBeVisible();
  });

  test('TC-AUTH-014: Duplicate Username', async ({ page }) => {
    await page.fill('input[name="username"]', 'existinguser');
    await page.fill('input[name="email"]', 'new@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.fill('input[name="confirmPassword"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Username already taken')).toBeVisible();
  });

  test('TC-AUTH-015: Weak Password Validation', async ({ page }) => {
    await page.fill('input[name="username"]', 'testuser');
    await page.fill('input[name="email"]', 'test@test.com');
    await page.fill('input[name="password"]', '123');
    await page.fill('input[name="confirmPassword"]', '123');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Password must be at least 8 characters')).toBeVisible();
  });

  test('TC-AUTH-016: Empty Registration Form', async ({ page }) => {
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Please fill in all required fields')).toBeVisible();
  });

  test('TC-AUTH-017: Invalid Email Format', async ({ page }) => {
    await page.fill('input[name="username"]', 'testuser');
    await page.fill('input[name="email"]', 'notanemail');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.fill('input[name="confirmPassword"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Please enter a valid email')).toBeVisible();
  });

  test('TC-AUTH-018: Username Too Short', async ({ page }) => {
    await page.fill('input[name="username"]', 'ab');
    await page.fill('input[name="email"]', 'test@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.fill('input[name="confirmPassword"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Username must be at least')).toBeVisible();
  });

  test('TC-AUTH-019: Special Characters in Username', async ({ page }) => {
    await page.fill('input[name="username"]', 'test@user!');
    await page.fill('input[name="email"]', 'test@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.fill('input[name="confirmPassword"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Username can only contain')).toBeVisible();
  });

  test('TC-AUTH-020: Registration Terms Agreement', async ({ page }) => {
    await page.fill('input[name="username"]', 'testuser');
    await page.fill('input[name="email"]', 'test@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.fill('input[name="confirmPassword"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Please agree to the terms')).toBeVisible();
  });
});

test.describe('Password Reset', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/forgot-password');
  });

  test('TC-AUTH-021: Forgot Password Form Loads', async ({ page }) => {
    await expect(page.locator('input[name="email"]')).toBeVisible();
    await expect(page.locator('text=Reset Password')).toBeVisible();
  });

  test('TC-AUTH-022: Forgot Password with Valid Email', async ({ page }) => {
    await page.fill('input[name="email"]', 'test@test.com');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Password reset link sent')).toBeVisible({ timeout: 5000 });
  });

  test('TC-AUTH-023: Forgot Password with Invalid Email', async ({ page }) => {
    await page.fill('input[name="email"]', 'notfound@test.com');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Email not found')).toBeVisible();
  });

  test('TC-AUTH-024: Reset Password Page Access', async ({ page }) => {
    await page.goto('/reset-password/test-token-123');
    await expect(page.locator('input[name="password"]')).toBeVisible();
    await expect(page.locator('input[name="confirmPassword"]')).toBeVisible();
  });

  test('TC-AUTH-025: Password Reset Success', async ({ page }) => {
    await page.goto('/reset-password/test-token-123');
    await page.fill('input[name="password"]', 'New@123456');
    await page.fill('input[name="confirmPassword"]', 'New@123456');
    await page.click('button[type="submit"]');
    await expect(page.locator('text=Password updated successfully')).toBeVisible();
  });
});

test.describe('Session Management', () => {
  test('TC-AUTH-026: Logout Functionality', async ({ page }) => {
    await page.goto('/profile');
    await page.click('text=Logout');
    await expect(page).toHaveURL(/.*login.*/);
  });

  test('TC-AUTH-027: Protected Route Redirect', async ({ page }) => {
    await page.goto('/profile');
    await expect(page).toHaveURL(/.*login.*/);
  });

  test('TC-AUTH-028: Session Timeout Warning', async ({ page }) => {
    await page.goto('/login');
    await page.fill('input[name="email"]', 'test@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await page.goto('/profile');
    await expect(page.locator('text=Your session will expire')).toBeVisible({ timeout: 30000 });
  });

  test('TC-AUTH-029: Max Login Attempts', async ({ page }) => {
    for (let i = 0; i < 5; i++) {
      await page.fill('input[name="email"]', 'test@test.com');
      await page.fill('input[name="password"]', 'wrongpassword');
      await page.click('button[type="submit"]');
      await page.waitForTimeout(500);
    }
    await expect(page.locator('text=Account locked')).toBeVisible();
  });

  test('TC-AUTH-030: Login Success After Lockout', async ({ page }) => {
    await page.goto('/login');
    await page.fill('input[name="email"]', 'test@test.com');
    await page.fill('input[name="password"]', 'Test@123456');
    await page.click('button[type="submit"]');
    await expect(page).toHaveURL(/.*profile.*/, { timeout: 10000 });
  });
});
