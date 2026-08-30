# CodeMesh Uninstaller (Windows / PowerShell)
# Removes CodeMesh .github folders from a target project.

param(
    [string]$Target = "."
)

$ErrorActionPreference = "Stop"

foreach ($folder in @('agents', 'skills', 'workflows', 'templates', 'instructions')) {
    $path = Join-Path $Target (Join-Path '.github' $folder)
    if (Test-Path $path) {
        Remove-Item -Path $path -Recurse -Force
        Write-Host "Removed $path" -ForegroundColor Yellow
    }
}

Write-Host "CodeMesh uninstalled." -ForegroundColor Green