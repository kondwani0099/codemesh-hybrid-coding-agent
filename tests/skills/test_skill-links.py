#!/usr/bin/env python3
"""Test that relative links in SKILL.md files resolve to real files."""

import re
import sys
from pathlib import Path

SKILLS_DIR = Path(__file__).resolve().parent.parent.parent / ".github" / "skills"


def test_skill_links_resolve():
    for skill_file in SKILLS_DIR.rglob("*.md"):
        text = skill_file.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target_path = target.split("#")[0]
            if not target_path:
                continue
            resolved = (skill_file.parent / target_path).resolve()
            assert resolved.exists(), f"{skill_file}: broken link -> {target}"


if __name__ == "__main__":
    test_skill_links_resolve()
    print("All skill link tests passed.")
    sys.exit(0)