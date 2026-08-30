# Summarization

## Purpose
Use small local models (e.g., Gemma 4B) to compress large content into concise, technical summaries.

## What to Summarize
- Source files.
- Test results / failure output.
- Architecture decisions.
- Errors and stack traces.
- Requirements.

## Summary Structure
A good file summary includes:

1. **Purpose** — what the file does.
2. **Key exports/symbols** — functions, classes, components.
3. **Data flow** — inputs, outputs, dependencies.
4. **Notable patterns** — conventions the implementer must follow.
5. **Caveats** — gotchas, TODOs, known issues.

## Rules
- Keep summaries technical, not narrative.
- Preserve names, paths, and line references.
- Never lose critical implementation details (schema changes, API signatures).
- Mark uncertainty explicitly rather than guessing.

## Example Prompt Shape
```
Summarize this file for a coding agent. Focus on: purpose, key symbols,
data flow, patterns to follow, and caveats. Preserve exact names and paths.
