import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week03.task05 import solve

class TestTask05(unittest.TestCase):
    def test_main(self):
        self.assertTrue(solve(3, 4, 5))
        self.assertFalse(solve(1, 1, 2))
        self.assertFalse(solve(-1, 2, 3))
