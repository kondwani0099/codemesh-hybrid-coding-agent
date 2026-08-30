# Ollama Setup

## Install Ollama
1. Download Ollama from the official site.
2. Run the installer.
3. Verify the server is running:
   ```bash
   ollama serve
   ```

## Pull Models
Pull the configured models (configurable — examples below):
```bash
ollama pull gemma4:4b
ollama pull qwen-coder
```

## Verify
```bash
curl http://localhost:11434/api/tags
```
Should list the installed models.

## Configure CodeMesh
Set the base URL and model names in `config/models.yaml`:

```yaml
models:
  analyzer:
    provider: ollama
    model: gemma4:4b
  summarizer:
    provider: ollama
    model: gemma4:4b
  local_coder:
    provider: ollama
    model: qwen-coder
  reviewer:
    provider: ollama
    model: gemma4:4b
```

## Check Connectivity
The engine should report:
- Ollama connected.
- Analyzer model available.
- Repository analysis ready.