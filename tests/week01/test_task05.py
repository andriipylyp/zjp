import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from course.week01.task05 import solve

class TestTask05(unittest.TestCase):
    def test_main(self):
        self.assertTrue(solve("AnAcoNda je super"))
        self.assertFalse(solve("python"))
