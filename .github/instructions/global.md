# Global Instructions

Rules every agent must understand and follow, regardless of role.

## Core Principles
- Protect user changes.
- Follow existing architecture.
- Do not invent APIs.
- Verify assumptions.
- Prefer minimal changes.
- Use tests.
- Never expose secrets.

## Local-First, Cloud-When-Necessary
- Use local models for analysis, summarization, and review.
- Escalate to cloud models only when required (see `model-routing` skill).
- Compress context before any cloud request (see `context-management` skill).

## Context Discipline
- Every agent must answer: **"What do I actually need to know to perform this task?"** before requesting additional context.
- Never blindly load the entire repository.
- Only forward relevant context.

## Communication
- Agents communicate through structured artifacts (see `templates/`).
- The output of one agent becomes the primary input of the next.

## Safety
- Dangerous commands require explicit approval.
- Never send secrets to cloud providers.
- Never auto-commit unless explicitly configured.