#!/usr/bin/env python3
"""Test that every skill directory contains a valid SKILL.md."""

import re
import sys
from pathlib import Path

SKILLS_DIR = Path(__file__).resolve().parent.parent.parent / ".github" / "skills"

REQUIRED_SECTIONS = ["Purpose", "Rules", "Validation"]


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


def test_every_skill_has_skill_md():
    for d in SKILLS_DIR.rglob("*"):
        if d.is_dir():
            skill_file = d / "SKILL.md"
            # Skip container directories (e.g., frontend/, backend/) that only
            # organize sub-skills.
            if not skill_file.exists() and any(c.is_dir() for c in d.iterdir()):
                continue
            assert skill_file.exists(), f"{d} missing SKILL.md"


def test_skill_md_valid():
    for d in SKILLS_DIR.rglob("*"):
        if not d.is_dir():
            continue
        skill_file = d / "SKILL.md"
        if not skill_file.exists():
            continue
        text = skill_file.read_text(encoding="utf-8")
        front = parse_frontmatter(text)
        assert front.get("name"), f"{skill_file} missing name"
        assert front.get("description"), f"{skill_file} missing description"
        for section in REQUIRED_SECTIONS:
            assert re.search(rf"^#+\s+{section}", text, re.MULTILINE), (
                f"{skill_file} missing section {section}"
            )


if __name__ == "__main__":
    test_every_skill_has_skill_md()
    test_skill_md_valid()
    print("All skill structure tests passed.")
    sys.exit(0)