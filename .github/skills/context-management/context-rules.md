# Context Rules

## Progressive Refinement
Always narrow context before expanding it:

```
Repository context
 → Relevant files
 → Relevant sections
 → Summary
 → Context package
```

## Rules of Engagement
1. **Start small.** Begin with file lists and summaries, not full file contents.
2. **Read selectively.** Read only the sections relevant to the task.
3. **Cache aggressively.** Store summaries in `.codemesh/summaries/` and reuse them.
4. **Never duplicate.** Do not send the same content twice.
5. **Remove irrelevance.** Strip boilerplate, generated code, and unrelated modules.
6. **Estimate tokens.** Estimate cost before every cloud request.

## What to Preserve
- Architectural decisions.
- Public API contracts.
- Data model relationships.
- Error-handling conventions.
- Security constraints.

## What to Omit
- Generated/vendor code.
- Comments and documentation that are not needed.
- Unrelated modules.
- Secrets and credentials.