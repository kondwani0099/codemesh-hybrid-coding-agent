# Escalation

## When to Escalate
- Local model confidence below threshold (< 0.70).
- High/critical complexity.
- Repeated local failures.
- Capability gaps (long context, advanced reasoning).
- Security-sensitive reasoning.

## Escalation Flow
```
confidence < 0.70
 → additional local analysis
 → still uncertain
 → cloud escalation
```

## Before Escalating
1. Compress context.
2. Estimate tokens and cost.
3. Select the appropriate cloud model.
4. Redact secrets.

## After Escalating
- Record the reason and cost.
- Feed results back into the local pipeline.

See `.github/skills/model-routing/escalation-policy.md`.