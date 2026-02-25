import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week01.task04 import solve

class TestTask04(unittest.TestCase):
    def test_main(self):
        self.assertEqual(solve("data.TXT"), "txt")
        self.assertEqual(solve("archive.tar.gz"), "gz")
        self.assertEqual(solve("README"), "")
