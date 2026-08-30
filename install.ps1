# CodeMesh — Reproducible Installer (Windows PowerShell)
#
# One-liner usage:
#   Set-ExecutionPolicy Bypass -Scope Process -Force; iwr -useb https://raw.githubusercontent.com/kondwani0099/codemesh-hybrid-coding-agent/v1.0.0/install.ps1 | iex
#
# Optional environment variables:
#   CODEMESH_TARGET      Project directory to install into  (default: current dir)
#   CODEMESH_TAG         Version tag to install             (default: v1.0.0)
#   CODEMESH_FORCE=1     Overwrite existing CodeMesh files
#   CODEMESH_NO_BACKUP=1 Do not back up existing states
#
# What it does:
#   1. Downloads the CodeMesh framework archive at the version tag.
#   2. Automatically backs up any existing CodeMesh files in the target
#      (<target>/.codemesh/backups/<timestamp>/).
#   3. Safely copies the managed files (.github/agents, skills, workflows,
#      templates, instructions) and per-project config into the target.
#   4. Validates schema integrity of the installed files.

$ErrorActionPreference = "Stop"

$owner = if ($env:CODEMESH_OWNER) { $env:CODEMESH_OWNER } else { "kondwani0099" }
$repo = if ($env:CODEMESH_REPO) { $env:CODEMESH_REPO } else { "codemesh-hybrid-coding-agent" }
$tag = if ($env:CODEMESH_TAG) { $env:CODEMESH_TAG } else { "v1.0.0" }
$target = if ($env:CODEMESH_TARGET) { $env:CODEMESH_TARGET } else { (Get-Location).Path }

$zipUrl = "https://github.com/$owner/$repo/archive/refs/tags/$tag.zip"
$tmpDir = Join-Path $env:TEMP "codemesh-install-$([guid]::NewGuid().ToString('N'))"
$zipPath = Join-Path $tmpDir "codemesh.zip"

New-Item -ItemType Directory -Force -Path $tmpDir | Out-Null

Write-Host "CodeMesh Reproducible Installer $tag" -ForegroundColor Cyan
Write-Host "Downloading CodeMesh $tag from $owner/$repo ..."
Invoke-WebRequest -Uri $zipUrl -OutFile $zipPath -UseBasicParsing

Write-Host "Extracting..."
Expand-Archive -Path $zipPath -DestinationPath $tmpDir -Force

# Locate the extracted framework directory (GitHub may name the archive
# folder <repo>-<tag> with or without the leading 'v' on the tag).
$src = $null
foreach ($d in (Get-ChildItem -Path $tmpDir -Directory)) {
    if (Test-Path (Join-Path $d.FullName ".github")) {
        $src = $d.FullName
        break
    }
}

if (-not $src) {
    Remove-Item -Recurse -Force $tmpDir -ErrorAction SilentlyContinue
    throw "Downloaded archive does not contain the CodeMesh framework."
}

$setup = Join-Path $src "scripts/setup.py"
$setupArgs = @($target)
if ($env:CODEMESH_FORCE -eq "1") { $setupArgs += "--force" }
if ($env:CODEMESH_NO_BACKUP -eq "1") { $setupArgs += "--no-backup" }

Write-Host "Installing into: $target"
& python $setup @setupArgs
$code = $LASTEXITCODE

Remove-Item -Recurse -Force $tmpDir -ErrorAction SilentlyContinue
if ($code -ne 0) {
    throw "CodeMesh installation failed with exit code $code."
}
