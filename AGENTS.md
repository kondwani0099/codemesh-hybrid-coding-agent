# AGENTS.md

## Graphify — Project Knowledge Graph

Graphify is the project's persistent knowledge graph. Use it as the first source of context for understanding the codebase, architecture, file relationships, documentation, and existing implementation decisions.

Repository: https://github.com/Graphify-Labs/graphify

---

## 1. Graphify Availability Check

Before doing substantial work on the project, check whether Graphify is available:

```bash
graphify --help
```

If the `graphify` command is unavailable, install it:

```bash
uv tool install graphifyy
```

Alternative:
```bash
pipx install graphifyy
```

If the command is still unavailable after installation, ensure the tool directory is on PATH.
For `uv`:
```bash
uv tool update-shell
```
For `pipx`:
```bash
pipx ensurepath
```
Then restart the terminal/session.

---

## 2. Install Graphify Agent Integration

If Graphify has not yet been integrated into this project, install the project-scoped integration.

For Codex:
```bash
graphify codex install --project
```

Generic Agent Skills installation:
```bash
graphify agents install
```

If using another supported coding agent, use its platform installer:
```bash
graphify claude install --project
graphify cursor install --project
graphify vscode install --project
graphify copilot install --project
graphify gemini install --project
graphify antigravity install --project
```

Only run the installer appropriate to the current coding environment.

---

## 3. Detect Existing Graph

Check whether:
```
graphify-out/
```
exists.

Important files include:
```
graphify-out/
├── graph.json
├── graph.html
└── GRAPH_REPORT.md
```

If these exist, use the existing graph before unnecessarily scanning the entire project again.

---

## 4. Build Graphify Context

If no graph exists, build one:
```bash
graphify .
```

For a deeper analysis:
```bash
graphify . --mode deep
```

For incremental updates after code changes:
```bash
graphify . --update
```

Do not rebuild the entire graph unnecessarily when `--update` is sufficient.

---

## 5. Query Graphify BEFORE Exploring the Codebase

For questions involving project architecture, modules, dependencies, relationships, implementation decisions, or unfamiliar code, query the graph first.

General query:
```bash
graphify query "QUESTION"
```

Example:
```bash
graphify query "How does authentication work in this project?"
```

For broad architectural questions, prefer BFS:
```bash
graphify query "How does the payment system connect to the database?"
```

For tracing a specific relationship/path:
```bash
graphify query "How does authentication reach the user database?" --dfs
```

Limit the returned context to conserve LLM tokens:
```bash
graphify query "How does authentication work?" --budget 1500
```

---

## 6. Explain Individual Concepts

Use:
```bash
graphify explain "CONCEPT"
```

Examples:
```bash
graphify explain "AuthService"
graphify explain "PaymentService"
graphify explain "User"
graphify explain "Postgres"
```

Use this before modifying unfamiliar components.

---

## 7. Trace Relationships

To find the shortest relationship between two concepts:
```bash
graphify path "CONCEPT_A" "CONCEPT_B"
```

Examples:
```bash
graphify path "User" "Database"
graphify path "PaymentService" "Invoice"
graphify path "AuthController" "UserRepository"
```

Use this to understand dependencies before changing connected components.

---

## 8. Update Graphify After Significant Changes

After substantial changes to the architecture, modules, APIs, database, configuration, or documentation, update the graph:

```bash
graphify . --update
```

Do not blindly rebuild the entire graph.

---

## 9. Watch Mode

For active development where automatic graph updates are useful:
```bash
graphify . --watch
```

Use watch mode only when it provides value; do not start persistent processes unnecessarily.

---

## 10. Generate Agent-Crawlable Wiki

When a human/agent-readable project knowledge base is useful:
```bash
graphify . --wiki
```

This generates an index and community-level articles that agents can crawl.

---

## 11. Visualization

Generate the standard visualization:
```bash
graphify .
```

Export SVG:
```bash
graphify . --svg
```

Export GraphML:
```bash
graphify . --graphml
```

Skip visualization when only machine-readable graph information is needed:
```bash
graphify . --no-viz
```

---

## 12. Database Graph Exports

Neo4j:
```bash
graphify . --neo4j
```

Push directly to Neo4j:
```bash
graphify . --neo4j-push bolt://localhost:7687
```

FalkorDB:
```bash
graphify . --falkordb
```

Push directly to FalkorDB:
```bash
graphify . --falkordb-push falkordb://localhost:6379
```

Do not connect to external graph databases unless explicitly required.

---

## 13. MCP Mode

When the coding agent needs Graphify through MCP:
```bash
graphify . --mcp
```

Use MCP when supported by the current agent/environment.

---

## 14. Add External Knowledge

Add a URL to the Graphify corpus:
```bash
graphify add "URL"
```

With author:
```bash
graphify add "URL" --author "Name"
```

With contributor:
```bash
graphify add "URL" --contributor "Name"
```

Use this for relevant external documentation, specifications, papers, or technical references that should become part of project context.

---

## 15. GitHub Repository Ingestion

Graphify can ingest another GitHub repository:
```bash
/graphify https://github.com/OWNER/REPO
```

Specific branch:
```bash
/graphify https://github.com/OWNER/REPO --branch BRANCH
```

Multiple repositories:
```bash
/graphify https://github.com/OWNER/REPO1 https://github.com/OWNER/REPO2
```

Use this when comparing or understanding external dependencies.

---

## Agent Operating Rules

### Rule 1 — Graph First
For substantial codebase questions:
1. Check `graphify-out/`.
2. If a graph exists, query it.
3. Use `graphify query`, `graphify explain`, or `graphify path`.
4. Then inspect the actual source files.
5. Never treat Graphify's inferred relationships as guaranteed facts.

### Rule 2 — Source Code Is Authoritative
Graphify provides context.
The actual source code, tests, configuration, migrations, and current runtime behavior remain authoritative.
If Graphify conflicts with source code:
`SOURCE CODE > TESTS > CONFIGURATION > GRAPHIFY INFERENCE`
Investigate the discrepancy.

### Rule 3 — Do Not Hallucinate Missing Architecture
If Graphify cannot answer a question, inspect the relevant files.
Do not invent modules, dependencies, APIs, or relationships.

### Rule 4 — Preserve Graph Context
After major architectural changes:
```bash
graphify . --update
```
Keep the graph synchronized with the project.

### Rule 5 — Use Deep Mode Selectively
Use:
```bash
graphify . --mode deep
```
when normal extraction does not provide enough architectural context.
Do not use deep mode for every small code change.

---

## Standard Development Workflow

For a new task:
1. Read `AGENTS.md`
2. Check Graphify availability (`graphify --help`)
3. Check `graphify-out/`
4. Query Graphify (`graphify query "..." --budget 1500`)
5. Inspect relevant source files
6. Understand dependencies (`graphify path "A" "B"`)
7. Plan change
8. Implement change
9. Run tests
10. Verify affected integrations
11. Update Graphify if architecture changed (`graphify . --update`)
12. Report what changed

---

## Graphify Failure Handling

If Graphify is unavailable:
- Do not stop the development task solely because Graphify is unavailable.
- Attempt installation (`uv tool install graphifyy` or `pipx install graphifyy`).
- If installation fails, continue using the repository directly.
- Report the Graphify failure clearly.
- Do not fabricate Graphify results.

If `graphify-out/` is missing:
```bash
graphify .
```

If the graph is stale:
```bash
graphify . --update
```

If the graph appears incomplete:
```bash
graphify . --mode deep
```

**Graphify Is a Context Layer, Not a Code Authority.**
Never modify code merely because Graphify suggests a relationship.
Always verify important relationships against the actual repository.
Use Graphify to reduce unnecessary file scanning, understand architecture, discover relationships, and maintain persistent project context while drastically cutting token consumption.
