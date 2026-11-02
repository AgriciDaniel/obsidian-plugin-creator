#!/usr/bin/env python3
"""Ensure README SVGs and GitHub token families reach the release secret gate."""
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("release", REPO / "scripts/package_release.py")
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


class ReleaseSecretScanTests(unittest.TestCase):
    def test_svg_file_and_archive_payload_reject_token_families(self) -> None:
        for prefix in ("gh" + kind + "_" for kind in "pousr"):
            payload = ("<svg><!-- " + prefix + "A" * 36 + " --></svg>").encode()
            with self.subTest(prefix=prefix):
                with self.assertRaisesRegex(SystemExit, "github token found"):
                    release.scan_bytes(payload, "source.zip:assets/readme/hero.svg", ".svg")
                with tempfile.TemporaryDirectory() as folder:
                    path = Path(folder) / "hero.svg"
                    path.write_bytes(payload)
                    with self.assertRaisesRegex(SystemExit, "github token found"):
                        release.scan_file(path, "assets/readme/hero.svg")

    def test_original_svg_assets_are_accepted(self) -> None:
        for name in ("hero.svg", "workflow.svg"):
            release.scan_file(REPO / "assets/readme" / name, name)


if __name__ == "__main__":
    unittest.main()
