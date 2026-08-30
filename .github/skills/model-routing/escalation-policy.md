# Escalation Policy

## Purpose
Define when local reasoning is insufficient and cloud escalation is justified.

## Escalation Triggers
- Local model confidence < threshold (e.g., 0.70).
- Task complexity is `high` or `critical`.
- Multiple failed local attempts.
- Task requires capabilities the local model lacks (e.g., very long context, advanced reasoning).
- Security-sensitive reasoning.

## Escalation Flow
```
confidence < 0.70
 → additional local analysis
 → still uncertain
 → cloud escalation
```

## Before Escalating
1. Compress context (see `context-management`).
2. Estimate tokens and cost.
3. Select the appropriate cloud model.
4. Redact secrets.

## After Escalation
- Record the escalation reason and cost.
- Feed results back to the local pipeline.