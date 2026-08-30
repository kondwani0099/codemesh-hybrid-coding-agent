# Architecture Overview

## Mental Model
CodeMesh is an agent-team framework. The core distinction:

```
AGENTS       SKILLS      WORKFLOWS
 WHO WORKS   KNOWLEDGE   HOW THEY
 ON IT       THEY USE    WORK TOGETHER
```

## System Diagram

```mermaid
graph TD
    A[User Request] --> O[CodeMesh Orchestrator]
    O --> W[Workflow Selection]
    W --> AN[Analyst]
    AN --> P[Planner]
    P --> C[Critic]
    P --> AR[Architect]
    P --> I[Implementer]
    I --> CR[Code Reviewer]
    I --> QA[QA Agent]
    QA --> UAT[UAT]
```

## Context Flow

```
Repository
 → File discovery
 → Relevance analysis
 → File summaries
 → Context compression
 → Cloud model (only when needed)
```

## Model Routing

```
Simple analysis → Local (Gemma 4B)
Complex implementation → Cloud
```

See `docs/architecture/agent-architecture.md` and `docs/architecture/model-architecture.md` for details.