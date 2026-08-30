# Handoff Rules

## Purpose
Define how agents communicate and pass work between each other.

## Core Rules
1. Agents communicate through structured artifacts (`.github/templates/`).
2. The output of one agent is the primary input of the next.
3. Hand off only necessary context — not everything known.
4. Use the `handoff.md` template for explicit handoffs.
5. Always reference artifact paths so the next agent can read them.

## Standard Handoff Chain
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

## What to Include
- What was done.
- What remains.
- Key decisions and constraints.
- Artifact locations.
- Open questions.

## What NOT to Include
- Full repository dumps.
- Redundant summaries already in artifacts.
- Secrets.

## Quality Gate Rule
- Never hand off across a quality gate (review → QA, QA → UAT) unless the gate passes.