#!/usr/bin/env python3
"""Test that workflow definitions contain the required structure."""

import re
import sys
from pathlib import Path

WORKFLOWS_DIR = Path(__file__).resolve().parent.parent.parent / ".github" / "workflows"

REQUIRED_SECTIONS = ["Purpose", "Flow", "Steps", "Artifacts"]


def test_workflows_have_required_sections():
    for path in WORKFLOWS_DIR.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        for section in REQUIRED_SECTIONS:
            assert re.search(rf"^#+\s+{section}", text, re.MULTILINE), (
                f"{path} missing section {section}"
            )


if __name__ == "__main__":
    test_workflows_have_required_sections()
    print("All workflow tests passed.")
    sys.exit(0)