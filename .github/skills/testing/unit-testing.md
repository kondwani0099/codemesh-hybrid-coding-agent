# Unit Testing

## Purpose
Test individual functions, classes, and components in isolation.

## Rules
- One behavior per test.
- Use descriptive test names.
- Mock external dependencies (network, DB, time).
- Test edge cases and error paths, not just the happy path.
- Keep tests fast and deterministic.

## Python (pytest)
```python
def test_invoice_can_be_approved():
    invoice = Invoice(status="pending")
    invoice.approve()
    assert invoice.is_approved is True
```

## Frontend (Vitest / Jest)
- Test component rendering and events.
- Mock API service calls.
- Assert on user-visible behavior.

## Validation
- `pytest` / `npm test` pass.
- Coverage added for new logic.