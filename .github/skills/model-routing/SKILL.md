---
name: model-routing
description: Defines how agents choose between local (Ollama) and cloud models based on task type, complexity, and cost policy.
---

# Model Routing Skill

## Purpose
Select the cheapest model that can reliably perform the task. Use local models for understanding and preparation; use cloud models only when superior reasoning or implementation is required.

## Routing Table

| Task | Model |
|------|-------|
| File summary | Local (Gemma 4B) |
| Repository indexing | Local (Gemma 4B) |
| Code explanation | Local (Gemma 4B) |
| Simple review | Local (Gemma 4B) |
| Simple bug | Local coder |
| Architecture | Cloud |
| Complex implementation | Cloud |
| Complex debugging | Cloud |
| Large refactor | Cloud |
| Security-sensitive reasoning | Cloud + human review |

## Rules
1. Prefer local models by default.
2. Escalate to cloud only when confidence is low or capability is insufficient.
3. Never send full repository context to the cloud (see `context-management`).
4. Track every request for cost reporting.
5. Model names are configurable — never hardcode.

See `routing-policy.md`, `escalation-policy.md`, and `cost-policy.md`.

## Validation
- Every cloud request must be preceded by a cost estimate.
- Local requests should represent the majority of model calls.