---
name: testing
description: Testing methodology — unit, integration, end-to-end, and regression — and when each is appropriate.
---

# Testing Skill

## Purpose
Define the testing methodology agents follow.

## Test Layers
- **Unit** — test a single function/component in isolation.
- **Integration** — test interactions between modules (DB, services, API).
- **End-to-End (E2E)** — test the full user journey through the UI.
- **Regression** — confirm existing behavior still works.

See `unit-testing.md`, `integration-testing.md`, and `e2e-testing.md`.

## When to Use Each
- Unit tests for logic and edge cases.
- Integration tests for data flow and API contracts.
- E2E for critical user journeys.
- Regression whenever behavior may be affected.

## Rules
- Write tests as features are implemented.
- Test behavior, not implementation details.
- Tests must be deterministic.
- Run the project's actual test commands (pytest, npm test) — detect them from project config before running.

## Validation
- The relevant test suite passes.
- New behavior has coverage.