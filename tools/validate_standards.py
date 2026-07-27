#!/usr/bin/env python3
"""Validate the minimum structure of the Ritru organisation standards repository."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "README.md",
    "profile/README.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    "LICENSE.md",
    ".github/CODEOWNERS",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/bug.yml",
    ".github/ISSUE_TEMPLATE/capability.yml",
    ".github/ISSUE_TEMPLATE/architecture-decision.yml",
    "docs/repository-standard.md",
    "docs/branch-and-merge-standard.md",
    "docs/ai-assisted-change-standard.md",
    "docs/security-baseline.md",
    "checklists/repository-bootstrap.md",
    "checklists/release-readiness.md",
)

PROHIBITED_MARKERS = ("TODO", "TBD", "CHANGEME")


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing required file: {relative}")
            continue
        content = path.read_text(encoding="utf-8")
        if not content.strip():
            errors.append(f"required file is empty: {relative}")
        if not content.endswith("\n"):
            errors.append(f"file must end with a newline: {relative}")
        for marker in PROHIBITED_MARKERS:
            if marker in content:
                errors.append(f"placeholder marker {marker!r} found in {relative}")

    for relative in (
        ".github/ISSUE_TEMPLATE/bug.yml",
        ".github/ISSUE_TEMPLATE/capability.yml",
        ".github/ISSUE_TEMPLATE/architecture-decision.yml",
    ):
        path = root / relative
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        if not content.startswith("name:"):
            errors.append(f"issue form must begin with name: {relative}")
        if "\nbody:\n" not in content:
            errors.append(f"issue form must define body: {relative}")

    profile = root / "profile/README.md"
    if profile.is_file() and "Ritru" not in profile.read_text(encoding="utf-8"):
        errors.append("organisation profile must identify Ritru")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Validated {len(REQUIRED_FILES)} required organisation-standard files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
