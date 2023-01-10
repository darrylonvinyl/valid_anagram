import unittest
from valid_anagram import verify_anagram

class TestValidAnagram(unittest.TestCase):
    def test_valid_anagram(self):
        self.assertEqual(verify_anagram("anagram","nagaram"), True)
        self.assertEqual(verify_anagram("rat","car"), False)
