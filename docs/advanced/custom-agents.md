# Custom Agents

## Creating a Custom Agent
1. Create `.github/agents/<category>/<name>.agent.md`.
2. Add YAML frontmatter:
   ```yaml
   ---
   name: my-agent
   description: When to use this agent.
   ---
   ```
3. Define role, rules, inputs, outputs, and handoffs.
4. Register it in `config/agents.yaml`.
5. Validate: `python scripts/validate-agents.py`.

## Best Practices
- Keep agents lightweight; put knowledge in skills.
- Give agents a clear, non-overlapping role.
- Define handoffs to and from existing agents.