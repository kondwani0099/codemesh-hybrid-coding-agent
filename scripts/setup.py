#!/usr/bin/env python3
"""CodeMesh Setup — v1.0.1

Automatically pulls the CodeMesh agent-team framework into a target project so
you can start using the agents right away.

Works on Windows, Linux, and macOS (requires Python 3.8+).

Usage:
    python scripts/setup.py [TARGET] [--force] [--no-backup]

    TARGET      Path to the project to install CodeMesh into (default: current dir).
    --force     Overwrite any existing files in the target .github/ folders.
    --no-backup Do not create a timestamped backup of existing CodeMesh files.

Examples:
    python  scripts/setup.py                     # install into the current dir
    python  scripts/setup.py ../my-app           # install into ../my-app
    python  scripts/setup.py ../my-app --force   # overwrite existing CodeMesh files

Windows PowerShell and Linux/macOS both run this same script, so behavior is
identical on every platform.
"""

from __future__ import annotations

import argparse
import datetime
import re
import shutil
import sys
from pathlib import Path

VERSION = "1.0.1"

# The framework folders (relative to the CodeMesh repo root) that are installed
# into the target project's .github/ directory.
FRAMEWORK_FOLDERS = [
    "agents",
    "skills",
    "workflows",
    "templates",
    "instructions",
]

# The config files (relative to the repo root) copied into the target project's
# .codemesh/config/ directory so each project can tweak its own models/costs.
CONFIG_FILES = [
    "codemesh.yaml",
    "models.yaml",
    "agents.yaml",
    "workflows.yaml",
    "costs.yaml",
]


def repo_root() -> Path:
    """Return the absolute path to the CodeMesh repository root."""
    return Path(__file__).resolve().parent.parent


def copy_tree(src: Path, dst: Path, force: bool, copied: list[str], skipped: list[str]) -> None:
    """Copy the contents of src into dst without clobbering unless --force."""
    if not src.is_dir():
        return
    for item in src.iterdir():
        target = dst / item.name
        if target.exists() and not force:
            skipped.append(str(target))
            continue
        if item.is_dir():
            shutil.copytree(item, target, dirs_exist_ok=True)
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, target)
        copied.append(str(target))


def backup_existing(target: Path) -> Path | None:
    """Snapshot existing managed CodeMesh files in the target before changes.

    Existing .github/{agents,skills,workflows,templates,instructions} and
    .codemesh/config are copied into <target>/.codemesh/backups/<timestamp>/.
    Returns the backup directory, or None if there was nothing to back up.
    """
    existing: list[Path] = []
    for folder in FRAMEWORK_FOLDERS:
        src = target / ".github" / folder
        if src.exists():
            existing.append(src)
    cfg = target / ".codemesh" / "config"
    if cfg.exists():
        existing.append(cfg)

    if not existing:
        return None

    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_dir = target / ".codemesh" / "backups" / stamp
    for src in existing:
        rel = src.relative_to(target)
        dst = backup_dir / rel
        shutil.copytree(src, dst, dirs_exist_ok=True)
    return backup_dir


def validate_target(target: Path) -> list[str]:
    """Verify schema integrity of the CodeMesh files installed in the target.

    Checks that every .agent.md has valid frontmatter (name + description) and
    that every leaf skill directory contains a SKILL.md. Returns a list of
    issues (empty when the installation is valid).
    """
    issues: list[str] = []

    agents_dir = target / ".github" / "agents"
    if agents_dir.is_dir():
        for path in sorted(agents_dir.rglob("*.agent.md")):
            text = path.read_text(encoding="utf-8", errors="ignore")
            m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
            if not m:
                issues.append(f"{path.relative_to(target)}: missing YAML frontmatter")
                continue
            front: dict[str, str] = {}
            for line in m.group(1).splitlines():
                if ":" in line:
                    key, _, value = line.partition(":")
                    front[key.strip()] = value.strip()
            if not front.get("name"):
                issues.append(f"{path.relative_to(target)}: agent missing `name`")
            if not front.get("description"):
                issues.append(f"{path.relative_to(target)}: agent missing `description`")

    skills_dir = target / ".github" / "skills"
    if skills_dir.is_dir():
        for d in sorted(skills_dir.rglob("*")):
            if not d.is_dir():
                continue
            is_leaf = not any(child.is_dir() for child in d.iterdir())
            if is_leaf and not (d / "SKILL.md").exists():
                issues.append(f"{d.relative_to(target)}: leaf skill dir missing SKILL.md")

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="codemesh-setup",
        description="Install the CodeMesh agent-team framework into a project.",
    )
    parser.add_argument("target", nargs="?", default=".", help="Target project path (default: current directory).")
    parser.add_argument("--force", action="store_true", help="Overwrite existing CodeMesh files.")
    parser.add_argument("--no-backup", action="store_true", help="Do not back up existing CodeMesh files.")
    parser.add_argument("--version", action="version", version=f"CodeMesh Setup {VERSION}")
    args = parser.parse_args()

    root = repo_root()
    target = Path(args.target).expanduser().resolve()

    if not root.joinpath(".github").is_dir():
        print(f"Error: could not locate the CodeMesh framework (missing {root / '.github'}).")
        print("Run this script from inside the CodeMesh repository.")
        return 1

    if target == root:
        print("Warning: target is the CodeMesh repository itself; no-op except reporting.")
    elif not target.is_dir():
        print(f"Creating project directory: {target}")
        target.mkdir(parents=True, exist_ok=True)

    print(f"CodeMesh Setup v{VERSION}")
    print(f"Installing into: {target}")
    print("=" * 60)

    # 0. Back up existing managed files before modifying anything.
    backup_dir = None if args.no_backup else backup_existing(target)
    if backup_dir:
        print(f"Backed up existing CodeMesh files to: {backup_dir}")
    else:
        print("No existing CodeMesh files to back up.")

    copied: list[str] = []
    skipped: list[str] = []

    # 1. Framework folders -> <target>/.github/
    for folder in FRAMEWORK_FOLDERS:
        src = root / ".github" / folder
        dst = target / ".github" / folder
        copy_tree(src, dst, args.force, copied, skipped)

    # 2. Config files -> <target>/.codemesh/config/
    cfg_src = root / "config"
    cfg_dst = target / ".codemesh" / "config"
    for name in CONFIG_FILES:
        src_file = cfg_src / name
        if not src_file.is_file():
            continue
        dst_file = cfg_dst / name
        if dst_file.exists() and not args.force:
            skipped.append(str(dst_file))
            continue
        cfg_dst.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_file, dst_file)
        copied.append(str(dst_file))

    print(f"\nCopied {len(copied)} items into {target}:")
    for item in copied:
        print(f"  + {item}")

    if skipped:
        print(f"\nSkipped {len(skipped)} existing items (use --force to overwrite):")
        for item in skipped:
            print(f"  ~ {item}")

    # 3. Validate schema integrity of the installed files.
    print("\nValidating schema integrity...")
    issues = validate_target(target)
    if issues:
        print(f"Validation FAILED with {len(issues)} issue(s):")
        for issue in issues:
            print(f"  ! {issue}")
        print("\nInstallation completed, but the installed files failed validation.")
        return 1

    print("Validation PASSED (agents frontmatter + skill structure).")

    print("\n" + "=" * 60)
    print("CodeMesh installed successfully.")
    print(f"\nNext steps:")
    print(f"  1. Open {target} in VS Code.")
    print(f"  2. Open Copilot Chat and select an agent (e.g. codemesh, planner, vue, python, qa).")
    print(f"  3. Tune models in {target / '.codemesh' / 'config' / 'models.yaml'}.")
    print("  4. Start a workflow, e.g. 'Add an approval workflow to invoices.'")
    return 0


if __name__ == "__main__":
    sys.exit(main())
