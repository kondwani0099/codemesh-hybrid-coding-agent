# Agent Rules

## Boundaries
- Each agent operates within its defined role (see `.github/agents/`).
- The orchestrator routes; specialist agents implement.
- Do not perform another agent's role unless explicitly asked.

## Roles Summary
| Agent | Owns |
|-------|------|
| codemesh | Routing/orchestration |
| analyst | Investigation and findings |
| planner | Implementation-ready plans |
| architect | Structural design |
| critic | Challenge plans |
| implementer | Code changes |
| code-reviewer | Review diffs |
| security | Security review |
| qa | Test validation, fix loop |
| uat | Acceptance verification |
| devops | Builds, CI/CD, deployment |
| documentation | Docs |
| retrospective | Lessons learned |

## Handoffs
- Hand off with the `handoff.md` template.
- State what the next agent needs to know, not everything known.
- Never hand off without artifacts when a template exists.

## Tool Discipline
- Use the minimum tools needed.
- Read before modifying.
- Validate after modifying.