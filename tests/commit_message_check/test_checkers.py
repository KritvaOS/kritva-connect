"""Tests for the commit message checkers copied from kritva-program (D-032, D-044)."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts" / "security"))
import check_commit_format as fmt  # noqa: E402
import check_commit_messages as sess  # noqa: E402

GOOD = "docs(contract): add draft v0.1 Connect contracts\n\nBody.\n\nTask: KOS-CONNECT-001\n"


class SessionTrailer(unittest.TestCase):
    def test_clean_message(self):
        self.assertEqual(sess.problems(GOOD), [])

    def test_trailer_rejected(self):
        self.assertTrue(sess.problems(GOOD + "Claude-Session: https://example.invalid/x\n"))

    def test_link_rejected(self):
        self.assertTrue(sess.problems("docs(x): y\n\nsee claude.ai/code/session_1\n\nTask: KOS-CONNECT-001\n"))

    def test_co_author_allowed(self):
        self.assertEqual(sess.problems(GOOD + "Co-Authored-By: A <a@example.invalid>\n"), [])


class Format(unittest.TestCase):
    def test_good(self):
        self.assertEqual(fmt.problems(GOOD), [])

    def test_tasks_list(self):
        self.assertEqual(fmt.problems("feat(x): y\n\nTasks: KOS-CONNECT-001, KOS-CONNECT-002\n"), [])

    def test_missing_footer(self):
        self.assertTrue(fmt.problems("docs(x): y\n\nBody only\n"))

    def test_bad_header(self):
        self.assertTrue(fmt.problems("Update stuff\n\nTask: KOS-CONNECT-001\n"))

    def test_two_footers(self):
        self.assertTrue(fmt.problems("docs(x): y\n\nTask: KOS-CONNECT-001\nTask: KOS-CONNECT-002\n"))

    def test_none_only_for_docs_or_chore(self):
        self.assertEqual(fmt.problems("chore(ci): y\n\nTasks: None (tooling)\n"), [])
        self.assertTrue(fmt.problems("feat(x): y\n\nTasks: None (tooling)\n"))

    def test_merge_commit_ignored(self):
        self.assertEqual(fmt.problems("Merge pull request #1 from a/b\n"), [])

    def test_session_trailer_rejected(self):
        self.assertTrue(fmt.problems(GOOD + "Claude-Session: https://example.invalid/x\n"))


if __name__ == "__main__":
    unittest.main()
