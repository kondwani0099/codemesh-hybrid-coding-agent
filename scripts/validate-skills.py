#!/usr/bin/env python3
"""Validate all CodeMesh skill structures.

Checks that every skill directory under .github/skills has:
- A SKILL.md file.
- Valid YAML frontmatter with `name` and `description`.
- Required sections (Purpose, Rules, Validation).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SKILLS_DIR = Path(__file__).resolve().parent.parent / ".github" / "skills"

REQUIRED_SECTIONS = ["Purpose", "Rules", "Validation"]
errors = []


def parse_frontmatter(text: str) -> dict:
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}
    front = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            front[key.strip()] = value.strip()
    return front


def main() -> int:
    skill_dirs = [d for d in SKILLS_DIR.rglob("*") if d.is_dir()]
    if not skill_dirs:
        print(f"No skill directories found under {SKILLS_DIR}")
        return 1

    for d in skill_dirs:
        skill_file = d / "SKILL.md"
        rel = d.relative_to(SKILLS_DIR.parent.parent)

        # Skip container directories (e.g., frontend/, backend/) that only
        # organize sub-skills and do not define a skill of their own.
        if not skill_file.exists():
            has_subdirs = any(child.is_dir() for child in d.iterdir())
            if has_subdirs:
                continue
            errors.append(f"{rel}: missing SKILL.md")
            continue

        text = skill_file.read_text(encoding="utf-8")
        front = parse_frontmatter(text)
        if not front.get("name"):
            errors.append(f"{rel}: SKILL.md missing frontmatter `name`")
        if not front.get("description"):
            errors.append(f"{rel}: SKILL.md missing frontmatter `description`")

        for section in REQUIRED_SECTIONS:
            if not re.search(rf"^#+\s+{section}", text, re.MULTILINE):
                errors.append(f"{rel}: SKILL.md missing required section `{section}`")

    if errors:
        print("Skill validation FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"All {len(skill_dirs)} skill directories validated successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())