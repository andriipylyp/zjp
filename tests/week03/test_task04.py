import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week03.task04 import solve

class TestTask04(unittest.TestCase):
    def test_main(self):
        self.assertTrue(solve(2000))
        self.assertFalse(solve(1900))
        self.assertTrue(solve(2024))
        self.assertFalse(solve(2023))
