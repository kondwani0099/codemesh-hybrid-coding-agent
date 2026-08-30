---
name: node
description: Node.js / TypeScript backend conventions, async patterns, and testing.
---

# Node Skill

## Purpose
Standard Node.js / TypeScript backend development knowledge.

## Rules
- Follow existing project structure and conventions.
- Use TypeScript with strict mode where applicable.
- Handle async errors correctly (`async/await`, `try/catch`, or a result type).
- Validate inputs (Zod, Joi, or manual).
- Avoid unnecessary dependencies.
- Write tests for new behavior.
- Maintain API compatibility.

## Patterns
- Module-per-concern.
- Service layer for business logic.
- Centralized error handling and middleware.
- Environment-based configuration (no hardcoded secrets).

## Async
- Prefer `async/await` over callbacks.
- Use connection pooling for databases.
- Handle unhandled rejections.

## Testing
- Use Vitest or Jest.
- Test with supertest for HTTP.
- Mock external services.

## Validation
- `npm test`
- `npm run lint`
- `npm run build` (type check)