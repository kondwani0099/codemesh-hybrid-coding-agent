# Example Workflow: Security Audit

## Request
> "Audit the authentication and authorization of the API."

## Agent Chain
```
Analyst → Security → Architect → Planner → Implementer → Security verification
```

## Findings Template
| Severity | Location | Description | Recommendation |
|----------|----------|-------------|----------------|
| High | file:line | Broken access control | Enforce role checks |
| Medium | file:line | Missing rate limiting | Add throttling |

## Escalation
Security-sensitive reasoning uses the cloud model + human review per the routing policy.