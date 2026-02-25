import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week02.task04 import solve

class TestTask04(unittest.TestCase):
    def test_main(self):
        self.assertEqual(solve("ha", 3), "ha-ha-ha")
        self.assertEqual(solve("x", 1), "x")
        self.assertEqual(solve("x", 0), "")
