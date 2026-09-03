# Graphify Setup & Lifecycle

Installation, IDE/agent integration, and graph lifecycle management commands.

---

## 1. Installation

### Recommended: UV Tool
```bash
uv tool install graphifyy
uv tool update-shell
```

### Alternative: Pipx
```bash
pipx install graphifyy
pipx ensurepath
```

---

## 2. Agent & IDE Integrations

Install project-scoped hooks and agent skills for the active development environment:

```bash
# VS Code / Copilot
graphify vscode install --project
graphify copilot install --project

# Codex (installs PreToolUse hook and AGENTS.md rules)
graphify codex install --project

# Claude / Cursor / Gemini / Antigravity
graphify claude install --project
graphify cursor install --project
graphify gemini install --project
graphify antigravity install --project

# Generic Agents skill
graphify agents install
```

---

## 3. Graph Building & Maintenance

### Initial Extraction
```bash
# Standard extraction
graphify .

# Deep architectural analysis
graphify . --mode deep
```

### Incremental Synchronization
Run after code changes or file modifications:
```bash
graphify . --update
```

### Watch Mode (Active Development)
```bash
graphify . --watch
```

---

## 4. Graph Artifacts

Graphify outputs all state into `graphify-out/`:
- `graphify-out/graph.json`: Machine-readable node and edge graph.
- `graphify-out/graph.html`: Interactive browser visualization.
- `graphify-out/GRAPH_REPORT.md`: Summary of detected components, communities, and circular dependencies.
