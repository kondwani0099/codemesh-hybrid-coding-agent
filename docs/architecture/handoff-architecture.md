# Handoff Architecture

## Purpose
Agents communicate through structured artifacts (templates). The output of one agent becomes the primary input of the next.

## Standard Chain
```
Analyst → analysis.md
Planner → plan.md
Architect → architecture.md
Security → security-review.md
Implementer → implementation.md
Code Reviewer → code-review.md
QA → qa.md
UAT → uat.md
Retrospective → retrospective.md
```

## Handoff Rules
- Hand off only necessary context.
- Reference artifact paths.
- Never cross a quality gate without it passing.
- Never include secrets or full repository dumps.

See `.github/instructions/handoff-rules.md`.