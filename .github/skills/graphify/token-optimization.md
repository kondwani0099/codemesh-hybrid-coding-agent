# Token Optimization & Graph Querying

Guide for leveraging Graphify queries to navigate large codebases while conserving LLM context tokens.

---

## 1. Why Graph-First Queries Save Tokens

Scanning full file trees and reading multi-thousand-line source files rapidly exhausts agent context windows. Querying Graphify first extracts precisely the required subgraphs, function call chains, and module dependencies in a few hundred tokens.

---

## 2. Querying Strategies

### Bounded Architectural Query
Always apply `--budget` to cap output tokens:
```bash
graphify query "How does authentication middleware validate JWT tokens?" --budget 1500
```

### BFS (Breadth-First Search) — System Overview
Best for answering wide architectural questions:
```bash
graphify query "How does the payment processing flow interact with the database?"
```

### DFS (Depth-First Search) — Trace Specific Path
Best for deep dependency paths:
```bash
graphify query "Trace the execution path from API route /login to password hasher" --dfs
```

---

## 3. Explaining Concepts

Before modifying unfamiliar classes, interfaces, or services:
```bash
graphify explain "AuthService"
graphify explain "PaymentController"
graphify explain "DatabasePool"
```

---

## 4. Tracing Shortest Dependency Paths

To understand how two components communicate without reading intermediary files:
```bash
graphify path "AuthController" "UserRepository"
graphify path "FrontendClient" "BackendAPI"
```

---

## 5. Crawlable Wiki Generation

Generate a lightweight, agent-crawlable markdown wiki:
```bash
graphify . --wiki
```
This generates indexed, community-level markdown articles that agents can inspect incrementally without bloating prompt context.
