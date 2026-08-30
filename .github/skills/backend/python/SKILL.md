---
name: python
description: Python conventions, type hints, async patterns, packaging, and testing.
---

# Python Skill

## Purpose
Standard Python backend development knowledge.

## Rules
- Follow existing project architecture.
- Use type hints everywhere.
- Handle exceptions correctly (catch specific exceptions, never bare `except`).
- Avoid unnecessary dependencies.
- Validate inputs.
- Use async where appropriate (I/O-bound work).
- Write tests for new behavior.
- Maintain API compatibility.

## Conventions
- Prefer `pathlib` over `os.path`.
- Use `dataclasses` or Pydantic for data structures.
- Use context managers for resources.
- Keep functions small and single-purpose.

## Packaging
- Use `pyproject.toml` (PEP 621).
- Declare dependencies explicitly.
- Pin versions for reproducibility where required.

## Testing
- Use pytest.
- Use fixtures for setup/teardown.
- Test async code with `pytest-asyncio`.
- Aim for behavior-based tests.

## Validation
- `pytest`
- `ruff check .`
- `mypy .` (where configured)