# Ollama Troubleshooting

## Out of Memory (OOM)
- Reduce `num_ctx` for the model.
- Close other model loads.
- Use a smaller model if the GPU is insufficient.

## GPU Memory
- Check `ollama ps` for loaded models.
- Unload unused models: `ollama stop <model>`.
- Consider CPU offload settings.

## Model Unavailable
- Error: `model '<name>' not found`.
- Fix: `ollama pull <name>`.
- Verify the name exactly matches the installed tag.

## Server Unavailable
- Error: connection refused on `localhost:11434`.
- Fix: start the server (`ollama serve`).
- Check firewall rules on non-local hosts.

## Timeouts
- Increase the client timeout for long generations.
- Reduce `num_predict`/`max_tokens`.
- Check network latency.

## Context Limits
- Error about context window exceeded.
- Reduce input length or increase `num_ctx`.
- Use summarization/compression (see `context-management`).

## Windows Issues
- Ensure Ollama is added to PATH.
- Use PowerShell; verify the service is running via `Get-Service ollama`.

## CUDA Issues
- Verify the GPU driver version.
- Check `ollama --version` and CUDA compatibility.
- Fall back to CPU mode (`OLLAMA_NUM_GPU=0`).