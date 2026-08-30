# Routing Policy

## Default Assignments

```
Simple analysis         → Gemma 4B (local)
Code explanation        → Gemma 4B (local)
Large code analysis     → Qwen Coder (local)
Complex architecture    → Cloud
Complex debugging       → Cloud
Critical security       → Strong cloud + human review
```

## Model Roles (configurable in config/models.yaml)

| Role | Default |
|------|---------|
| analyzer | gemma4:4b |
| summarizer | gemma4:4b |
| local_coder | qwen-coder |
| planner | cloud (configurable) |
| implementer | cloud (configurable) |
| reviewer | gemma4:4b |

## Decision Inputs
- Task type (`question`, `bug_fix`, `feature`, `refactor`, `architecture`, `security`, ...).
- Complexity (`low`, `medium`, `high`, `critical`).
- Required context size.
- Cost budget.