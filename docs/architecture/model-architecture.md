# Model Architecture

## The Core Idea
**Local-first, cloud-when-necessary.**

Use local models (Ollama) for understanding and preparation; use cloud models only when superior reasoning or implementation is required.

## Model Roles
| Role | Default | Provider |
|------|---------|----------|
| analyzer | gemma4:4b | ollama |
| summarizer | gemma4:4b | ollama |
| local_coder | qwen-coder | ollama |
| reviewer | gemma4:4b | ollama |
| planner | configurable | cloud |
| implementer | configurable | cloud |
| debugger | configurable | cloud |

## Routing Decision
```
Task type + complexity + context size + budget
 → model selection
```

## Escalation
Escalate to cloud when:
- Confidence is low.
- Complexity is high/critical.
- Local attempts fail repeatedly.
- Security-sensitive reasoning is required.

See `docs/models/model-strategy.md` and `.github/skills/model-routing/`.