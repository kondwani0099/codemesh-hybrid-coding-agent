# Delivery Agents

## DevOps Agent
Handles builds, Docker, CI/CD, deployment, and release preparation. See `.github/agents/delivery/devops.agent.md`.

## Documentation Agent
Handles API docs, README updates, and developer documentation. See `.github/agents/delivery/documentation.agent.md`.

## Graphify Setup Agent
Installs, initializes, updates, and manages the project's Graphify knowledge graph, IDE integrations, and MCP services. See `.github/agents/delivery/graphify-setup.agent.md`.

## Retrospective Agent
Reflects on completed work and records lessons learned. See `.github/agents/delivery/retrospective.agent.md`.

## Principles
- Update docs as features are implemented.
- Keep the project knowledge graph synchronized with architectural changes.
- Never auto-deploy to production without approval.
- Capture lessons for future agents.