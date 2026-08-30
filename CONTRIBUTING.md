# Contributing

Thank you for your interest in contributing to CodeMesh! This project is an
agent-team framework. Contributions of many kinds are welcome.

## Ways to Contribute

- **Create new agents** — add `.agent.md` files under `.github/agents/`.
- **Improve skills** — add or edit `SKILL.md` files under `.github/skills/`.
- **Define workflows** — add workflow docs under `.github/workflows/`.
- **Improve templates** — edit files under `.github/templates/`.
- **Fix documentation** — update files under `docs/`.
- **Report bugs** — open an issue describing the problem and expected behavior.

## Creating an Agent

1. Choose the correct category folder (e.g., `frontend/`, `backend/`, `quality/`).
2. Create a `.agent.md` file with YAML frontmatter:
   ```yaml
   ---
   name: my-agent
   description: One-line description of when to use this agent.
   ---
   ```
3. Document the agent's role, rules, inputs, outputs, and handoffs.
4. Run `python scripts/validate-agents.py` to verify the agent definition.

## Creating a Skill

1. Create a folder under `.github/skills/`.
2. Add a `SKILL.md` with the skill's purpose, when to use it, rules, and validation.
3. Run `python scripts/validate-skills.py` to verify the skill structure.

## Testing

Run the validation suite:

```bash
python scripts/validate-agents.py
python scripts/validate-skills.py
python scripts/check-links.py
pytest
```

## Pull Request Process

1. Keep changes focused and well documented.
2. Update `CHANGELOG.md`.
3. Ensure all validations pass.
4. Reference related issues in your PR description.