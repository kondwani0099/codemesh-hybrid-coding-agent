# CodeMesh Installer (Windows / PowerShell)
# Copies .github/agents, .github/skills, .github/workflows into the target project.

param(
    [string]$Target = ".",
    [switch]$Force
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot

function Copy-Dir {
    param([string]$Source, [string]$Dest)
    if (Test-Path $Dest) {
        if (-not $Force) {
            Write-Host "Destination exists: $Dest (use -Force to overwrite)" -ForegroundColor Yellow
            return
        }
    }
    New-Item -ItemType Directory -Force -Path $Dest | Out-Null
    Copy-Item -Path (Join-Path $Source '*') -Destination $Dest -Recurse -Force
    Write-Host "Copied $Source -> $Dest" -ForegroundColor Green
}

Write-Host "Installing CodeMesh into $Target" -ForegroundColor Cyan
Copy-Dir (Join-Path $RepoRoot '.github\agents') (Join-Path $Target '.github\agents')
Copy-Dir (Join-Path $RepoRoot '.github\skills') (Join-Path $Target '.github\skills')
Copy-Dir (Join-Path $RepoRoot '.github\workflows') (Join-Path $Target '.github\workflows')
Copy-Dir (Join-Path $RepoRoot '.github\templates') (Join-Path $Target '.github\templates')
Copy-Dir (Join-Path $RepoRoot '.github\instructions') (Join-Path $Target '.github\instructions')

Write-Host "CodeMesh installed successfully." -ForegroundColor Green