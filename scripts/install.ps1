# CodeMesh Installer (Windows / PowerShell)
# Delegates to the cross-platform setup.py so Linux and Windows behave identically.

param(
    [string]$Target = ".",
    [switch]$Force
)

$ErrorActionPreference = "Stop"
$Setup = Join-Path $PSScriptRoot "setup.py"

if (-not (Test-Path $Setup)) {
    Write-Host "Error: setup.py not found next to install.ps1" -ForegroundColor Red
    exit 1
}

$Args = @($Target)
if ($Force) { $Args += "--force" }

Write-Host "Running CodeMesh Setup (cross-platform)..." -ForegroundColor Cyan
& python $Setup @Args
exit $LASTEXITCODE