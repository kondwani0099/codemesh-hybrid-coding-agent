# Project Setup

## Recommended Repository Layout
```
project/
├── backend/          # Python / FastAPI
│   ├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── tests/
├── frontend/         # Vue / TypeScript
│   ├── src/
│   │   ├── components/
│   │   ├── views/
│   │   ├── stores/
│   │   └── services/
│   └── tests/
└── .github/          # CodeMesh (installed)
    ├── agents/
    ├── skills/
    ├── workflows/
    ├── templates/
    └── instructions/
```

## Recommended Config
- `config/models.yaml` — set your Ollama model names.
- `config/costs.yaml` — set cloud provider rates.
- `config/codemesh.yaml` — toggle context, routing, and security options.

## Best Practices
- Add `.codemesh/` to `.gitignore` (it stores local cache).
- Keep agent definitions lightweight; put knowledge in skills.
- Commit the CodeMesh `.github/` folders so all collaborators share the same agents.