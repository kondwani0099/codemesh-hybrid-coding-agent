# Agent Output

This directory is for **example/runtime outputs** from CodeMesh agent runs — not permanent source code.

## Example
```
agent-output/
└── 042/
    ├── analysis.md
    ├── plan.md
    ├── architecture.md
    ├── implementation.md
    ├── review.md
    ├── qa.md
    └── uat.md
```

## Notes
- Keep this directory empty in the repository (see `.gitkeep`).
- Runtime outputs should be git-ignored or stored outside the repo.

## Generated Indexes
Run `python scripts/generate-index.py --write` to write agent/skill/workflow index files here.