---
name: documentation
description: Documentation conventions — API docs, README, architecture docs, and developer documentation.
---

# Documentation Skill

## Purpose
Produce and maintain clear, accurate documentation.

## Rules
- Update docs as features are implemented.
- Keep API docs in sync with code.
- Document decisions and trade-offs.
- Never document secrets.
- Use the `documentation` templates where relevant.

## What to Document
- Public APIs and contracts.
- Architecture decisions (with reasons).
- Setup and development instructions.
- Workflows and agent behavior.
- Breaking changes.

## Validation
- Docs reflect the current code.
- Links resolve (run `scripts/check-links.py`).
- No secrets in docs.