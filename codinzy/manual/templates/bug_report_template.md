# Bug Report Template

## Defect Information

| Field | Value |
|-------|-------|
| **DEF-ID** | DEF-001 |
| **Module** | Payments |
| **Severity** | Critical / High / Medium / Low |
| **Priority** | P0 / P1 / P2 / P3 |
| **Status** | New / Open / In Progress / Resolved / Closed |
| **Reported By** | [Tester Name] |
| **Reported Date** | YYYY-MM-DD |
| **Assigned To** | [Developer Name] |
| **Fixed Date** | YYYY-MM-DD |

---

## Defect Summary

### Title
Clear and concise title describing the issue

### Description
Provide a detailed description of the bug:

1. **What happened?**
   - Description of the unexpected behavior

2. **What should have happened?**
   - Description of the expected behavior

3. **Steps to Reproduce**
   - Step-by-step instructions to reproduce the issue

4. **Frequency**
   - [ ] Always
   - [ ] Sometimes
   - [ ] Once
   - [ ] Intermittent

---

## Environment Details

| Parameter | Value |
|-----------|-------|
| **Browser** | Chrome 120 / Firefox 121 / Safari 17 |
| **OS** | Windows 11 / macOS Sonoma / iOS 17 |
| **App Version** | v2.4.1 |
| **Build Number** | 1234 |
| **Environment** | Production / Staging / Development |
| **Device Type** | Desktop / Mobile / Tablet |

---

## Steps to Reproduce

| Step | Action | Expected Result | Actual Result |
|------|--------|-----------------|---------------|
| 1 | Navigate to Payments page | Payment dashboard loads | ✓ |
| 2 | Click "Add Payment Method" | Modal opens | ✓ |
| 3 | Enter invalid card details | Validation error shown | ✗ Crashes |

---

## Test Data Used

```json
{
    "card_number": "4242424242424242",
    "expiry": "12/25",
    "cvc": "123"
}
```

---

## Evidence

### Screenshot
![Bug Screenshot](path/to/screenshot.png)

### Video Recording
[Video Link](path/to/recording.mp4)

### Error Message
```
TypeError: Cannot read property 'amount' of null
    at PaymentProcessor.validateTransaction (payment.js:245)
    at PaymentProcessor.process (payment.js:189)
```

### Console Logs
```
[ERROR] 2026-01-20 14:30:15 - PaymentProcessor: Invalid payment method
[ERROR] 2026-01-20 14:30:16 - Uncaught TypeError: Cannot read property 'amount' of null
```

### Network Logs
```json
{
    "request": {
        "method": "POST",
        "url": "/api/payments/process/",
        "status": 500
    },
    "response": {
        "error": "Internal Server Error"
    }
}
```

---

## Root Cause Analysis

### Primary Cause
[Description of the root cause]

### Contributing Factors
- Factor 1
- Factor 2
- Factor 3

---

## Suggested Fix

```python
# Proposed code fix
def validate_payment_method(payment_data):
    if payment_data.get('amount') is None:
        raise ValidationError("Payment amount is required")
    # Rest of validation logic
```

---

## Impact Assessment

### User Impact
- **Number of Users Affected**: [Estimate]
- **Business Impact**: High / Medium / Low
- **Revenue Impact**: [Description]

### Technical Impact
- **Data Integrity**: Yes / No
- **Security Risk**: Yes / No
- **Performance Impact**: Yes / No

---

## Related Information

### Related Defects
- DEF-045 (Similar issue)
- DEF-089 (Same root cause)

### Related Test Cases
- TC-PAY-001
- TC-PAY-015

### Workaround
[If available, describe a workaround for the issue]

---

## Resolution

### Resolution Date
YYYY-MM-DD

### Resolution Summary
[Description of how the defect was resolved]

### Verification Steps
1. Step 1
2. Step 2
3. Step 3

### Verified By
[Name]

---

## Comments

| Date | Author | Comment |
|------|--------|---------|
| YYYY-MM-DD | Tester | Initial report |
| YYYY-MM-DD | Developer | Investigating |
| YYYY-MM-DD | Developer | Fix implemented |
| YYYY-MM-DD | Tester | Verified and closed |
