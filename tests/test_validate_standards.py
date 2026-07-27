from __future__ import annotations

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.validate_standards import REQUIRED_FILES, validate


class ValidateStandardsTests(unittest.TestCase):
    def _valid_tree(self, root: Path) -> None:
        for relative in REQUIRED_FILES:
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            if relative.startswith(".github/ISSUE_TEMPLATE/") and relative != ".github/ISSUE_TEMPLATE/config.yml":
                content = "name: Example\ndescription: Example\nbody:\n  - type: markdown\n"
            elif relative == "profile/README.md":
                content = "# Ritru\n"
            else:
                content = "# Valid content\n"
            path.write_text(content, encoding="utf-8")

    def test_valid_tree_passes(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self._valid_tree(root)
            self.assertEqual(validate(root), [])

    def test_missing_file_fails(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self._valid_tree(root)
            (root / "SECURITY.md").unlink()
            self.assertTrue(any("SECURITY.md" in error for error in validate(root)))

    def test_placeholder_fails(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self._valid_tree(root)
            (root / "README.md").write_text("# TODO\n", encoding="utf-8")
            self.assertTrue(any("TODO" in error for error in validate(root)))


if __name__ == "__main__":
    unittest.main()
