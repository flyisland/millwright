"""Isolated script regression tests; never use the real home skill directory."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


class LinkSkillsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="millwright-link-test-")
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        self.repo = root / "repo"
        self.home = root / "home"
        self.home.mkdir()
        (self.repo / "scripts").mkdir(parents=True)
        self.script = self.repo / "scripts/link-skills.sh"
        shutil.copy(Path(__file__).resolve().parents[1] / "scripts/link-skills.sh", self.script)
        self.source = self.repo / "skills/example"
        self.source.mkdir(parents=True)
        (self.source / "SKILL.md").write_text("fixture", encoding="utf-8")
        self.dest = self.home / ".agents/skills"
        self.env = dict(os.environ, HOME=str(self.home))

    def run_script(self, answer=""):
        return subprocess.run(["bash", str(self.script)], env=self.env,
                              input=answer, text=True, capture_output=True, timeout=5)

    def conflict(self):
        target = self.dest / "example"
        target.mkdir(parents=True)
        note = target / "local-notes.txt"
        note.write_text("preserve", encoding="utf-8")
        return note

    def test_normal_and_repeat(self):
        for _ in range(2):
            result = self.run_script()
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual((self.dest / "example").resolve(), self.source.resolve())

    def test_conflict_eof_and_rejection_preserve_data(self):
        note = self.conflict()
        for answer in ("", "no\n", "y\n"):
            result = self.run_script(answer)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("permanently deleted", result.stderr)
            self.assertTrue(note.is_file())
            self.assertFalse((self.dest / "example").is_symlink())

    def test_explicit_approval_replaces_directory(self):
        note = self.conflict()
        result = self.run_script("yes\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(note.exists())
        self.assertTrue((self.dest / "example").is_symlink())
        self.assertTrue((self.source / "SKILL.md").is_file())

    def test_direct_repo_symlink_cannot_be_overridden(self):
        self.dest.parent.mkdir()
        self.dest.symlink_to(self.repo / "skills", target_is_directory=True)
        result = self.run_script("yes\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("resolves into this repository", result.stderr)
        self.assertFalse(self.source.is_symlink())

    def test_parent_repo_symlink_retry_rechecks(self):
        self.dest.parent.symlink_to(self.repo, target_is_directory=True)
        result = self.run_script("retry\nyes\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stderr.count("resolves into this repository"), 2)
        self.assertFalse(self.source.is_symlink())
        self.assertTrue((self.source / "SKILL.md").is_file())

    def test_external_parent_symlink_is_supported(self):
        external = self.home / "external"
        external.mkdir()
        self.dest.parent.symlink_to(external, target_is_directory=True)
        result = self.run_script()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((external / "skills/example").is_symlink())

    def test_dangling_destination_fails_safely(self):
        self.dest.parent.mkdir()
        self.dest.symlink_to(self.home / "missing")
        result = self.run_script("yes\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("not a usable directory", result.stderr)
        self.assertFalse((self.home / "missing").exists())


if __name__ == "__main__":
    unittest.main()
