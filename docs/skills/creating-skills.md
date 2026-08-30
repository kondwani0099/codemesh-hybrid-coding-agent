# Creating Skills

## When to Create a Skill
- Reusable knowledge used by multiple agents.
- Stack-specific conventions.
- Process rules (routing, context, safety).

## Authoring
1. Create a directory under `.github/skills/`.
2. Add a `SKILL.md` with YAML frontmatter:
   ```yaml
   ---
   name: my-skill
   description: One-line description.
   ---
   ```
3. Include sections: **Purpose**, **When to Use**, **Rules**, **Validation**.
4. Add supporting `.md` files for detail.

## Validation
Run:
```bash
python scripts/validate-skills.py
```

## Naming
- Use `kebab-case` for directories.
- Keep `SKILL.md` focused; move depth into supporting files.