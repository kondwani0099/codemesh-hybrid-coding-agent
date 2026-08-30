# End-to-End Testing

## Purpose
Test complete user journeys through the real UI.

## Rules
- Cover critical user journeys (login, create, approve, submit).
- Use Playwright/Cypress for browser automation.
- Keep E2E suites small and focused (they are slow and flaky).
- Use stable selectors and test IDs.
- Isolate E2E from external services with fixtures.

## When to Use
- Critical business flows.
- Release validation.
- Regression across the full stack.

## Validation
- E2E suite passes for the defined journeys.