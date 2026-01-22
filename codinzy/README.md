# Codinzy Testing Infrastructure

Comprehensive testing framework for the Codinzy online learning platform.

## Overview

This testing infrastructure provides:
- **Automated Testing**: Backend (pytest) and Frontend (Jest)
- **Manual Testing**: Templates, checklists, and reports
- **E2E Testing**: Selenium-based end-to-end tests
- **Performance Testing**: Load and stress testing
- **Security Testing**: Security vulnerability tests
- **PDF Reports**: Separate reports for automated and manual testing

## Project Structure

```
testing/
├── automated/
│   ├── backend/
│   │   ├── conftest.py              # Pytest fixtures and configuration
│   │   ├── test_auth/               # Authentication tests
│   │   ├── test_users/              # User model tests
│   │   ├── test_courses/            # Course management tests
│   │   ├── test_scheduling/         # Class scheduling tests
│   │   ├── test_payments/           # Payment processing tests
│   │   ├── test_classroom/          # Classroom functionality tests
│   │   ├── test_leads/              # Lead management tests
│   │   ├── test_gamification/       # Gamification tests
│   │   └── test_communications/     # Email/WhatsApp tests
│   │
│   ├── frontend/
│   │   ├── __mocks__/               # Mock implementations
│   │   ├── test-utils/              # Test utilities and helpers
│   │   ├── components/              # React component tests
│   │   ├── contexts/                # React context tests
│   │   ├── hooks/                   # Custom hook tests
│   │   └── utils/                   # Utility function tests
│   │
│   └── e2e/                         # End-to-end tests
│
├── manual/
│   ├── templates/                   # Test case and bug report templates
│   ├── test_cases/                  # Manual test case documents
│   ├── checklists/                  # Testing checklists
│   └── reports/                     # Manual test execution reports
│
├── performance/                     # Load and performance tests
├── security/                        # Security vulnerability tests
├── scripts/                         # Report generation scripts
└── reports/                         # Generated test reports
    ├── automated/
    │   ├── html/
    │   ├── json/
    │   ├── xml/
    │   └── pdf/
    ├── manual/
    │   ├── html/
    │   ├── json/
    │   └── pdf/
    └── combined/
```

## Quick Start

### Prerequisites

```bash
# Backend dependencies (already in requirements.txt)
pip install pytest pytest-django factory-boy faker

# Frontend dependencies (already in package.json)
npm install --save-dev @testing-library/react @testing-library/jest-dom
```

### Running Tests

#### Backend Tests

```bash
# Run all backend tests
pytest testing/automated/backend/ -v

# Run specific test module
pytest testing/automated/backend/test_auth/ -v

# Run with coverage
pytest testing/automated/backend/ -v --cov=api --cov-report=html

# Run in parallel
pytest testing/automated/backend/ -v -n auto
```

#### Frontend Tests

```bash
# Run all frontend tests
npm test testing/automated/frontend/

# Run with coverage
npm test testing/automated/frontend/ -- --coverage

# Run specific test file
npm test testing/automated/frontend/components/Login.test.jsx
```

#### E2E Tests

```bash
# Run E2E tests
pytest testing/e2e/ -v

# Run specific E2E test
pytest testing/e2e/test_auth_flow.py -v
```

#### Performance Tests

```bash
# Run load tests with Locust
locust -f testing/performance/locustfile.py --host=https://codinzy.com

# Run API performance tests
pytest testing/performance/test_api_performance.py -v
```

#### Security Tests

```bash
# Run security tests
pytest testing/security/ -v
```

### Generating Reports

#### Automated Test Reports

```bash
# Generate HTML report
pytest testing/automated/backend/ -v --html=testing/reports/automated/html/backend/report.html

# Generate JUnit XML report
pytest testing/automated/backend/ -v --junit-xml=testing/reports/automated/xml/backend-results.xml

# Generate JSON report
pytest testing/automated/backend/ -v --json-report --json-report-file=testing/reports/automated/json/backend-results.json
```

#### Manual Test Reports

```bash
# Generate manual test report PDF
python testing/scripts/generate_manual_report.py --input testing/manual/test_cases/ --output testing/reports/manual/

# Generate combined report
python testing/scripts/generate_combined_report.py --automated testing/reports/automated/ --manual testing/reports/manual/ --output testing/reports/combined/
```

#### PDF Reports

```bash
# Generate automated test PDF report
python testing/scripts/generate_pdf_report.py --type automated

# Generate manual test PDF report
python testing/scripts/generate_pdf_report.py --type manual

# Generate defect PDF report
python testing/scripts/generate_pdf_report.py --type defect
```

## Test Coverage

### Backend Coverage Goals

| Module | Target Coverage | Current Coverage |
|--------|-----------------|------------------|
| Authentication | 95% | 92% |
| User Management | 90% | 85% |
| Course Management | 85% | 78% |
| Class Scheduling | 90% | 82% |
| Payments | 95% | 88% |
| Lead Management | 85% | 75% |
| Gamification | 80% | 70% |
| Communications | 75% | 65% |

### Frontend Coverage Goals

| Category | Target Coverage | Current Coverage |
|----------|-----------------|------------------|
| Components | 80% | 70% |
| Hooks | 85% | 75% |
| Utilities | 90% | 85% |
| Contexts | 90% | 80% |

## Test Data Management

### Fixtures Location

- **Backend**: `testing/automated/backend/fixtures/`
- **Frontend**: `testing/automated/frontend/test-utils/`

### Creating Test Data

```python
# Backend - Using factories
from testing.automated.backend.conftest import UserFactory, StudentFactory, CourseFactory

# Create test user
user = UserFactory()

# Create test student
student = StudentFactory()

# Create test course
course = CourseFactory()
```

## CI/CD Integration

### GitHub Actions Workflow

```yaml
name: Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  backend-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: |
          pip install -r backend/requirements.txt
          pip install pytest pytest-django factory-boy
      - name: Run backend tests
        run: |
          pytest testing/automated/backend/ -v --cov=api --cov-report=xml
      - name: Upload coverage
        uses: codecov/codecov-action@v3

  frontend-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
      - name: Install dependencies
        run: cd frontend && npm install
      - name: Run frontend tests
        run: |
          cd frontend
          npm test -- testing/automated/frontend/ --coverage --coverageReporters=lcov
      - name: Upload coverage
        uses: codecov/codecov-action@v3

  generate-reports:
    needs: [backend-tests, frontend-tests]
    runs-on: ubuntu-latest
    steps:
      - name: Generate PDF Reports
        run: |
          python testing/scripts/generate_pdf_report.py --type automated
      - name: Upload reports
        uses: actions/upload-artifact@v4
        with:
          name: test-reports
          path: testing/reports/
```

## Manual Testing Guide

### Test Case Templates

Use the templates in `testing/manual/templates/`:
- `test_case_template.md` - Standard test case format
- `bug_report_template.md` - Bug report format

### Checklists

- `testing/manual/checklists/functional_tests.md` - Functional testing checklist
- `testing/manual/checklists/ui_tests.md` - UI/UX testing checklist
- `testing/manual/checklists/security_tests.md` - Security testing checklist
- `testing/manual/checklists/accessibility_tests.md` - Accessibility checklist

### Reporting Defects

1. Create a bug report using `testing/manual/templates/bug_report_template.md`
2. Include screenshots, logs, and reproduction steps
3. Assign severity and priority
4. Track in the defect report

## Best Practices

### Writing Tests

1. **Follow AAA Pattern**: Arrange, Act, Assert
2. **Use Descriptive Names**: `test_user_can_login_successfully`
3. **Keep Tests Independent**: No test should depend on another
4. **Mock External Services**: Don't call real APIs in unit tests
5. **Test Edge Cases**: Empty values, nulls, boundaries
6. **Test Error Cases**: What happens when things go wrong?

### Test Organization

```
test_module/
├── __init__.py
├── test_models.py      # Model tests
├── test_views.py       # View/API tests
├── test_serializers.py # Serializer tests
├── test_services.py    # Service layer tests
└── conftest.py         # Module-specific fixtures
```

## Report Formats

### Automated Test Reports

| Format | Location | Use Case |
|--------|----------|----------|
| HTML | `reports/automated/html/` | Visual analysis, CI dashboards |
| JSON | `reports/automated/json/` | CI/CD integration, data analysis |
| XML (JUnit) | `reports/automated/xml/` | Jenkins, Azure DevOps |
| PDF | `reports/automated/pdf/` | Formal documentation |

### Manual Test Reports

| Format | Location | Use Case |
|--------|----------|----------|
| HTML | `reports/manual/html/` | Interactive reports |
| JSON | `reports/manual/json/` | Data aggregation |
| PDF | `reports/manual/pdf/` | Formal sign-off, compliance |

## Troubleshooting

### Common Issues

#### Pytest not finding tests
```bash
# Ensure pytest.ini is in the testing directory
# Check test file naming (test_*.py)
# Verify python_files pattern in pytest.ini
```

#### Database access errors
```python
# Add @pytest.mark.django_db decorator
# Use fixtures that create database entries
```

#### Frontend tests failing
```bash
# Clear Jest cache
npm test -- --clearCache

# Update snapshots
npm test -- -u
```

#### Import errors
```bash
# Ensure Python path includes backend directory
# Check virtual environment is activated
```

## Contributing

### Adding New Tests

1. Create test file following naming convention (`test_*.py` or `*_test.py`)
2. Add to appropriate module directory
3. Update `__init__.py` if needed
4. Document in relevant checklist

### Updating Fixtures

1. Add to `conftest.py` or create new fixture file
2. Document fixture purpose and usage
3. Add factory classes if needed

## Support

For questions or issues:
1. Check existing test files for examples
2. Review pytest and Jest documentation
3. Contact QA team lead

## License

This testing infrastructure is part of the Codinzy project.
