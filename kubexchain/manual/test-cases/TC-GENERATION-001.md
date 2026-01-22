# Test Case: Generation Profit Calculation

| Field | Value |
|-------|-------|
| **Test Case ID** | TC-GENERATION-001 |
| **Module** | Generations |
| **Sub-Module** | Profit Calculation |
| **Test Priority** | Critical |
| **Test Type** | Functional |
| **Created By** | QA Team |
| **Created Date** | 2026-01-20 |
| **Last Updated** | 2026-01-20 |

---

## Test Objective

Verify that generation profit is calculated correctly using the formula:
```
Generation Profit = Σ (commissionAmount × 0.001 × days_since_created)
```

For each generation record, the profit accumulates at 0.10% daily from the commission date.

---

## Pre-requisites

- User with generation records (team commissions)
- Generation records with commission amounts and creation dates

---

## Test Data

| Field | Value |
|-------|-------|
| Username | `rashedul01` |
| Generation Records | 38 records |
| Total Commission | $955.79 |
| Total Generation Profit | $43.97 |

---

## Test Steps

| Step | Action | Expected Result | Pass/Fail |
|------|--------|-----------------|-----------|
| 1 | Login as admin | Admin dashboard loads | [ ] |
| 2 | Navigate to Users > rashedul01 | User profile displays | [ ] |
| 3 | View generation records | List of commissions shown | [ ] |
| 4 | Select a generation record | Record details displayed | [ ] |
| 5 | Note commission amount | e.g., $400.80 | [ ] |
| 6 | Note commission date | e.g., Dec 5, 2025 | [ ] |
| 7 | Calculate days elapsed | Today - Commission Date = 46 days | [ ] |
| 8 | Calculate expected profit | $400.80 × 0.001 × 46 = $18.44 | [ ] |
| 9 | Compare with displayed profit | Values match | [ ] |
| 10 | Repeat for multiple records | All calculations match | [ ] |
| 11 | Sum all generation profits | Total = $43.97 | [ ] |
| 12 | Verify API returns same value | API: generationEarnings = $43.97 | [ ] |

---

## Test Environment

| Field | Value |
|-------|-------|
| Browser | Chrome |
| Browser Version | 120.0 |
| Operating System | Windows 11 |
| API Endpoint | /api/auth/me-detailed |

---

## Test Execution

| Field | Value |
|-------|-------|
| Executed By | QA Tester |
| Execution Date | 2026-01-20 |
| Environment | Staging |

---

## Test Results

| Status | Result |
|--------|--------|
| [ ] Pass | All steps executed successfully |
| [ ] Fail | One or more steps failed |
| [ ] Blocked | Test cannot be executed |

---

## Generation Profit Calculation Details

| Commission | Date | Days | 0.10% Daily | Profit |
|------------|------|------|-------------|--------|
| $400.80 | Dec 5, 2025 | 46 | 0.001 | $18.4368 |
| $400.80 | Dec 5, 2025 | 46 | 0.001 | $18.4368 |
| $50.10 | Dec 5, 2025 | 46 | 0.001 | $2.3046 |
| $19.40 | Dec 5, 2025 | 46 | 0.001 | $0.8924 |
| $10.10 | Dec 4, 2025 | 47 | 0.001 | $0.4747 |
| ... | ... | ... | ... | ... |
| **Total** | | | | **$43.97** |

---

## Verification Formula

```javascript
const generationProfit = generations.reduce((sum, gen) => {
  const days = Math.floor((today - new Date(gen.createdAt)) / (1000 * 60 * 60 * 24));
  return sum + (gen.commissionAmount * 0.001 * days);
}, 0);
```

---

## Defects/Bugs Found

| Defect ID | Description | Severity | Status |
|-----------|-------------|----------|--------|
| N/A | | | |

---

## Notes

- Generation profit is NOT the sum of all commissions
- Generation profit is the daily accumulation (0.10% per day) of each commission
- The longer a commission has been active, the more generation profit it earns

---

## Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Tester | | | |
| Reviewer | | | |
