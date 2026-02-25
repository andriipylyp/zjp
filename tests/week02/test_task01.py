import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week02.task01 import solve

class TestTask01(unittest.TestCase):
    def test_main(self):
        self.assertEqual(solve(3, 4), 7)
        self.assertEqual(solve(-2, 5), 3)
