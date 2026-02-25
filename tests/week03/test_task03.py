import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week03.task03 import solve

class TestTask03(unittest.TestCase):
    def test_main(self):
        self.assertEqual(solve(90), "A")
        self.assertEqual(solve(89), "B")
        self.assertEqual(solve(50), "E")
        self.assertEqual(solve(49), "FX")
