# Integration Testing

## Purpose
Test interactions between modules: services ↔ database, API ↔ services, frontend ↔ backend.

## Rules
- Use a real or in-memory database for DB tests.
- Exercise the full request path (HTTP → service → DB → response).
- Verify contracts between layers.
- Clean up test data between tests.

## Examples
- API endpoint tests (FastAPI TestClient / supertest).
- Repository/service integration tests.
- Frontend service layer tests against a mock API.

## Validation
- Integration suite passes.
- Contracts validated across layers.