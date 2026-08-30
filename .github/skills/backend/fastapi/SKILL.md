---
name: fastapi
description: FastAPI conventions — routes, Pydantic schemas, dependencies, middleware, auth, and async.
---

# FastAPI Skill

## Purpose
Standard FastAPI backend development knowledge.

## Rules
- Follow existing project structure (routes, schemas, services).
- Use Pydantic models for request/response validation.
- Keep route handlers thin; put logic in services.
- Use dependency injection for shared dependencies (DB, auth, config).
- Use async endpoints for I/O-bound work.
- Maintain OpenAPI compatibility.
- Handle errors with HTTPException and proper status codes.

## Structure
```
app/
├── main.py
├── api/routes/...
├── api/schemas/...
├── services/...
└── models/...
```

## Patterns
- Router-per-resource.
- Pydantic `BaseModel` schemas with `ConfigDict(from_attributes=True)` for ORM.
- Middleware for CORS, logging, and auth.
- Background tasks for slow work.

## Auth
- Use OAuth2/ JWT or API keys depending on the project.
- Protect routes with dependencies.
- Never log tokens or secrets.

## Validation
- `pytest`
- `ruff check .`
- OpenAPI schema is valid.