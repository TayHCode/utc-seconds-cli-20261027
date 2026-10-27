"""Exercise the public CLI through a real Python subprocess."""
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CLITests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run([sys.executable, "-B", str(ROOT / "utc_delta.py"), *args],
                              capture_output=True, text=True, cwd=ROOT)

    def test_signed_whole_seconds(self):
        cases = [
            ("2026-10-27T00:00:00Z", "2026-10-27T00:01:05Z", "65\n"),
            ("2026-10-27T00:01:05Z", "2026-10-27T00:00:00Z", "-65\n"),
            ("2026-10-27T00:00:00Z", "2026-10-27T00:00:00Z", "0\n"),
            ("2024-02-28T23:59:59Z", "2024-03-01T00:00:00Z", "86401\n"),
            ("0001-01-01T00:00:00Z", "9999-12-31T23:59:59Z", "315537897599\n"),
        ]
        for start, end, expected in cases:
            with self.subTest(start=start, end=end):
                result = self.run_cli(start, end)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout, expected)
                self.assertEqual(result.stderr, "")

    def test_rejects_malformed_timestamps_in_either_position(self):
        valid = "2026-10-27T00:00:00Z"
        invalid = ["bad", "2026-02-29T00:00:00Z", "0000-01-01T00:00:00Z",
                   "2026-13-01T00:00:00Z", "2026-10-27T24:00:00Z",
                   "2026-10-27T00:00:60Z", "2026-1-27T00:00:00Z",
                   "2026-10-27 00:00:00Z", "2026-10-27T00:00:00z",
                   "2026-10-27T00:00:00+00:00", "2026-10-27T00:00:00.1Z",
                   "2026-10-27T00:00:00Z\n", " 2026-10-27T00:00:00Z",
                   "２０２６-10-27T00:00:00Z"]
        for value in invalid:
            for args in [(value, valid), (valid, value)]:
                with self.subTest(args=args):
                    result = self.run_cli(*args)
                    self.assertEqual(result.returncode, 2)
                    self.assertEqual(result.stdout, "")
                    self.assertIn("error:", result.stderr)
                    self.assertNotIn("Traceback", result.stderr)

    def test_missing_argument(self):
        result = self.run_cli("2026-10-27T00:00:00Z")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("required", result.stderr)


if __name__ == "__main__":
    unittest.main()
