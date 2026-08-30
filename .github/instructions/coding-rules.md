# Coding Rules

## General
- Follow existing project conventions and architecture.
- Make the smallest change that satisfies the requirement.
- Do not make unrelated changes.
- Prefer reusable components/helpers over duplication.

## Backend (Python/FastAPI/Node)
- Use type hints / TypeScript types.
- Handle exceptions/errors correctly.
- Validate inputs.
- Use async where appropriate.
- Keep route handlers thin; put logic in services.
- Maintain API compatibility.

## Frontend (Vue/React)
- Use existing component patterns.
- Avoid unnecessary global state.
- Handle loading and error states.
- Reuse components.
- Preserve responsive design and accessibility.

## Database
- Pair schema changes with migrations.
- Consider existing data.
- Use indexes for real query patterns.

## Tests
- Write tests as features are implemented.
- Test behavior, not implementation details.
- Run the project's actual test commands.

## Validation Commands
Detect and run the project's tools (do not assume):
- Python: `pytest`, `ruff`, `mypy`
- Vue/Node: `npm test`, `npm run lint`, `npm run build`
- Inspect `pyproject.toml`, `requirements.txt`, `package.json`, `Makefile`, `README` first.