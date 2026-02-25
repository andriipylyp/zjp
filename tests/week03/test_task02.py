import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week03.task02 import solve

class TestTask02(unittest.TestCase):
    def test_main(self):
        self.assertEqual(solve(1, 2, 3), 3)
        self.assertEqual(solve(10, -5, 7), 10)
        self.assertEqual(solve(-1, -2, -3), -1)
