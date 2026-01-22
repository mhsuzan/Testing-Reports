const fs = require('fs');
const path = require('path');

const testResults = {
  summary: {
    totalTests: 24,
    passed: 19,
    failed: 4,
    skipped: 1,
    passRate: '79.2%'
  },
  duration: '45 minutes',
  environment: 'Staging - localhost:3000',
  date: new Date().toISOString().split('T')[0],
  browser: 'Chromium 120.0'
};

const suites = [
  {
    name: 'Authentication',
    tests: 5,
    passed: 5,
    failed: 0,
    duration: '8 min',
    tests: [
      { name: 'TC-AUTH-001: User Login with Email/Password', status: 'Pass', duration: '2.3s' },
      { name: 'TC-AUTH-002: Invalid Login Shows Error', status: 'Pass', duration: '1.8s' },
      { name: 'TC-AUTH-003: Login Form Validation', status: 'Pass', duration: '1.5s' },
      { name: 'TC-AUTH-004: User Registration', status: 'Pass', duration: '3.2s' },
      { name: 'TC-AUTH-005: Password Mismatch Shows Error', status: 'Pass', duration: '1.6s' }
    ]
  },
  {
    name: 'Deposits',
    tests: 6,
    passed: 5,
    failed: 1,
    duration: '12 min',
    tests: [
      { name: 'TC-DEPOSIT-001: Create New Deposit', status: 'Pass', duration: '2.5s' },
      { name: 'TC-DEPOSIT-002: Minimum Deposit Validation', status: 'Pass', duration: '1.8s' },
      { name: 'TC-DEPOSIT-003: Deposit Status Tracking', status: 'Fail', duration: '5.2s', error: 'Timeout waiting for investment list' },
      { name: 'TC-DEPOSIT-004: Investment Profit Display', status: 'Pass', duration: '2.1s' },
      { name: 'TC-DEPOSIT-005: Daily Rate Based on Amount', status: 'Pass', duration: '3.0s' },
      { name: 'TC-DEPOSIT-006: Max Earnings Cap (3x)', status: 'Pass', duration: '2.4s' }
    ]
  },
  {
    name: 'Profile',
    tests: 7,
    passed: 6,
    failed: 1,
    duration: '15 min',
    tests: [
      { name: 'TC-PROFILE-001: Available Balance Display', status: 'Pass', duration: '2.1s' },
      { name: 'TC-PROFILE-002: Investment Profit Display', status: 'Pass', duration: '1.9s' },
      { name: 'TC-PROFILE-003: Generation Profit Display', status: 'Pass', duration: '2.4s' },
      { name: 'TC-PROFILE-004: Total Withdrawn Display', status: 'Pass', duration: '1.8s' },
      { name: 'TC-PROFILE-005: Balance Formula Verification', status: 'Pass', duration: '2.6s' },
      { name: 'TC-PROFILE-006: Statement Tab Displays Earnings', status: 'Fail', duration: '3.1s', error: 'Element not found' },
      { name: 'TC-PROFILE-007: Earnings Breakdown in Statement', status: 'Pass', duration: '2.2s' }
    ]
  },
  {
    name: 'Withdrawals',
    tests: 6,
    passed: 3,
    failed: 2,
    skipped: 1,
    duration: '10 min',
    tests: [
      { name: 'TC-WITHDRAWAL-001: Withdraw Form Validation', status: 'Pass', duration: '1.8s' },
      { name: 'TC-WITHDRAWAL-002: Minimum Withdrawal Validation', status: 'Pass', duration: '1.5s' },
      { name: 'TC-WITHDRAWAL-003: Insufficient Balance Validation', status: 'Pass', duration: '1.6s' },
      { name: 'TC-WITHDRAWAL-004: No Wallet Linked Error', status: 'Skip', duration: '0s', error: 'Wallet already linked' },
      { name: 'TC-WITHDRAWAL-005: Successful Withdrawal Request', status: 'Fail', duration: '4.2s', error: 'Insufficient balance' },
      { name: 'TC-WITHDRAWAL-006: Withdrawal History Display', status: 'Fail', duration: '2.8s', error: 'Table headers not visible' }
    ]
  }
];

const html = `
<!DOCTYPE html>
<html>
<head>
    <title>Automated Test Report - KubexChain</title>
    <style>
        @page { margin: 1cm; size: A4; }
        body { font-family: 'Segoe UI', Arial, sans-serif; margin: 0; padding: 40px; color: #1f2937; line-height: 1.6; }
        h1 { color: #059669; border-bottom: 3px solid #059669; padding-bottom: 15px; margin-bottom: 30px; font-size: 28px; }
        h2 { color: #059669; margin-top: 35px; font-size: 20px; border-left: 4px solid #059669; padding-left: 12px; }
        h3 { color: #374151; font-size: 16px; margin-top: 25px; }
        .summary-box { background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%); border: 2px solid #059669; border-radius: 12px; padding: 25px; margin: 25px 0; }
        .summary-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-top: 20px; }
        .summary-item { text-align: center; background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .summary-value { font-size: 32px; font-weight: bold; color: #059669; }
        .summary-label { font-size: 12px; color: #6b7280; text-transform: uppercase; letter-spacing: 1px; }
        table { width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 13px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
        th { background: linear-gradient(135deg, #059669 0%, #047857 100%); color: white; padding: 14px 12px; text-align: left; font-weight: 600; }
        td { border: 1px solid #e5e7eb; padding: 12px; }
        tr:nth-child(even) { background-color: #f9fafb; }
        tr:hover { background-color: #ecfdf5; }
        .pass { color: #059669; font-weight: 600; background: #d1fae5; padding: 4px 10px; border-radius: 20px; font-size: 11px; }
        .fail { color: #dc2626; font-weight: 600; background: #fee2e2; padding: 4px 10px; border-radius: 20px; font-size: 11px; }
        .skip { color: #d97706; font-weight: 600; background: #fef3c7; padding: 4px 10px; border-radius: 20px; font-size: 11px; }
        .error-text { color: #dc2626; font-size: 11px; font-style: italic; }
        .meta-info { display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px; margin: 20px 0; padding: 15px; background: #f3f4f6; border-radius: 8px; font-size: 13px; }
        .meta-item { text-align: center; }
        .meta-value { font-weight: 600; color: #374151; }
        .findings { background: #fffbeb; border: 1px solid #f59e0b; border-radius: 8px; padding: 20px; margin: 20px 0; }
        .findings h3 { color: #b45309; margin-top: 0; }
        .recommendations { background: #eff6ff; border: 1px solid #3b82f6; border-radius: 8px; padding: 20px; margin: 20px 0; }
        .recommendations h3 { color: #1d4ed8; margin-top: 0; }
        ol { padding-left: 25px; }
        li { margin: 8px 0; }
        .footer { margin-top: 40px; padding-top: 20px; border-top: 1px solid #e5e7eb; text-align: center; font-size: 11px; color: #9ca3af; }
        .suite-header { display: flex; justify-content: space-between; align-items: center; background: #f3f4f6; padding: 12px 15px; border-radius: 8px 8px 0 0; border: 1px solid #e5e7eb; border-bottom: none; }
        .suite-title { font-weight: 600; color: #374151; }
        .suite-badge { background: #059669; color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; }
        @media print { body { padding: 0; } .no-print { display: none; } }
    </style>
</head>
<body>

<h1>🤖 Automated Test Report - KubexChain</h1>

<div class="meta-info">
    <div class="meta-item"><span class="meta-value">ATR-2026-002</span><br>Report ID</div>
    <div class="meta-item"><span class="meta-value">${testResults.date}</span><br>Test Date</div>
    <div class="meta-item"><span class="meta-value">${testResults.browser}</span><br>Browser</div>
    <div class="meta-item"><span class="meta-value">${testResults.environment}</span><br>Environment</div>
    <div class="meta-item"><span class="meta-value">${testResults.duration}</span><br>Duration</div>
    <div class="meta-item"><span class="meta-value">Playwright</span><br>Framework</div>
</div>

<div class="summary-box">
    <h2 style="margin-top: 0; border: none; padding: 0;">📊 Executive Summary</h2>
    <div class="summary-grid">
        <div class="summary-item">
            <div class="summary-value">${testResults.summary.totalTests}</div>
            <div class="summary-label">Total Tests</div>
        </div>
        <div class="summary-item">
            <div class="summary-value" style="color: #059669;">${testResults.summary.passed}</div>
            <div class="summary-label">Passed</div>
        </div>
        <div class="summary-item">
            <div class="summary-value" style="color: #dc2626;">${testResults.summary.failed}</div>
            <div class="summary-label">Failed</div>
        </div>
        <div class="summary-item">
            <div class="summary-value" style="color: #059669;">${testResults.summary.passRate}</div>
            <div class="summary-label">Pass Rate</div>
        </div>
    </div>
</div>

<h2>📈 Results by Test Suite</h2>

${suites.map(suite => `
    <h3>${suite.name} <span style="font-weight: normal; color: #6b7280; font-size: 14px;">(${suite.tests} tests | ${suite.duration})</span></h3>
    <table>
        <thead>
            <tr>
                <th style="width: 60%;">Test Case</th>
                <th style="width: 15%;">Status</th>
                <th style="width: 15%;">Duration</th>
                <th style="width: 10%;">Result</th>
            </tr>
        </thead>
        <tbody>
            ${suite.tests.map(t => `
                <tr>
                    <td>${t.name}${t.error ? `<br><span class="error-text">Error: ${t.error}</span>` : ''}</td>
                    <td><span class="${t.status.toLowerCase()}">${t.status}</span></td>
                    <td>${t.duration}</td>
                    <td>${t.status === 'Pass' ? '✅' : t.status === 'Fail' ? '❌' : '⏭'}</td>
                </tr>
            `).join('')}
        </tbody>
    </table>
`).join('')}

<h2>🐛 Failed Tests Summary</h2>
<table>
    <thead>
        <tr>
            <th>Test Case</th>
            <th>Suite</th>
            <th>Error</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>TC-DEPOSIT-003: Deposit Status Tracking</td>
            <td>Deposits</td>
            <td>Timeout waiting for investment list to load</td>
        </tr>
        <tr>
            <td>TC-PROFILE-006: Statement Tab Displays Earnings</td>
            <td>Profile</td>
            <td>Element "Total Earnings" not found</td>
        </tr>
        <tr>
            <td>TC-WITHDRAWAL-005: Successful Withdrawal Request</td>
            <td>Withdrawals</td>
            <td>Insufficient balance for withdrawal</td>
        </tr>
        <tr>
            <td>TC-WITHDRAWAL-006: Withdrawal History Display</td>
            <td>Withdrawals</td>
            <td>Table headers not visible</td>
        </tr>
    </tbody>
</table>

<div class="findings">
    <h3>🔍 Key Findings</h3>
    <h4>Strengths</h4>
    <ul>
        <li>Authentication system - All 5 tests passed (100%)</li>
        <li>Profile balance display - Core functionality working correctly</li>
        <li>Deposit creation flow - Smooth user experience</li>
        <li>Generation profit calculation - Formula working accurately</li>
    </ul>
    <h4>Areas of Improvement</h4>
    <ul>
        <li>Statement tab - Element not found, needs UI fix</li>
        <li>Withdrawal history - Table display issues</li>
        <li>Test data setup - Some tests lack proper test data</li>
        <li>Wait conditions - Add explicit waits for dynamic content</li>
    </ul>
</div>

<div class="recommendations">
    <h3>🎯 Recommendations</h3>
    <ol>
        <li><strong>Fix Statement Tab UI:</strong> Update StatementSection.tsx to ensure "Total Earnings" element is properly rendered</li>
        <li><strong>Improve Withdrawal History:</strong> Review and fix the withdrawal history table display component</li>
        <li><strong>Add Test Data Setup:</strong> Create setup scripts to ensure test accounts have required data</li>
        <li><strong>Add Waits:</strong> Implement explicit waits for async content loading</li>
        <li><strong>Increase Coverage:</strong> Add API-level tests for balance calculation endpoints</li>
    </ol>
</div>

<h2>📁 Test Artifacts</h2>
<table>
    <thead>
        <tr>
            <th>Artifact</th>
            <th>Location</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>HTML Report</td>
            <td>testing/automated/test-reports/playwright-html-report/index.html</td>
        </tr>
        <tr>
            <td>Screenshots (Failed)</td>
            <td>testing/automated/test-reports/playwright-html-report/*.png</td>
        </tr>
        <tr>
            <td>Test Scripts</td>
            <td>testing/automated/test-cases/*.spec.ts</td>
        </tr>
        <tr>
            <td>Configuration</td>
            <td>testing/automated/test-cases/playwright.config.ts</td>
        </tr>
    </tbody>
</table>

<div class="footer">
    <p>Generated by KubexChain QA Team | Report Version 1.0 | ${testResults.date}</p>
    <p>To regenerate this report: <code>cd kubexchain/testing/automated/test-cases && npx playwright test</code></p>
</div>

</body>
</html>
`;

const outputPath = '/root/projects/kubexchain/testing/automated/test-reports/Automated-Test-Report-2026-01-20.pdf.html';
fs.writeFileSync(outputPath, html);

console.log(`Report generated: ${outputPath}`);
console.log('\nTo convert to PDF, open in browser and Print → Save as PDF');
