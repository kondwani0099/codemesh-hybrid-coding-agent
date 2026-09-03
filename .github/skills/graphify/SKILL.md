---
name: graphify
description: Reusable knowledge graph workflows, Graphify CLI setup, token-optimized graph querying, relationship tracing, and codebase navigation.
---

# Graphify Skill

## Purpose
Enables agents to use Graphify as a persistent project knowledge graph to understand architecture, dependencies, and component relationships while drastically reducing LLM token consumption before inspecting source files.

## Core Areas
- **Setup & Installation**: CLI installation (`uv tool install graphifyy`), IDE agent integrations, graph creation (`graphify .`), and incremental updates (`setup.md`).
- **Token Optimization & Querying**: Budget-bounded queries (`--budget`), BFS/DFS path traversal, concept explanations, and wiki crawling (`token-optimization.md`).
- **Agent Operating Rules**: Graph-first search, source code authority hierarchy, and synchronization rules.

## Rules
- Query Graphify (`graphify query`, `graphify explain`, `graphify path`) before scanning entire directories or large source files to save context tokens.
- Always apply `--budget` limits on broad queries (e.g. `--budget 1500`).
- Source code is always authoritative over inferred graph relationships:
  `SOURCE CODE > TESTS > CONFIGURATION > GRAPHIFY INFERENCE`.
- Run `graphify . --update` after major architectural, structural, or API changes.
- Never block a critical task solely because Graphify is unavailable; fallback to direct file reading and report the status.

## Validation
- `graphify --help` executes cleanly when installed.
- `graphify-out/` directory contains updated `graph.json` and `GRAPH_REPORT.md`.
- Token-bounded queries return accurate, compact architectural context.
