import unittest
from valid_anagram import verify_anagram

class TestTask(unittest.TestCase):
    def test_contains_duplicate(self):
        self.assertEqual(verify_anagram("anagram","nagaram"), True)
        self.assertEqual(verify_anagram("rat","car"), False)
