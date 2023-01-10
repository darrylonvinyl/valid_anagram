"""Leetcode - 242 - Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

1) Create letter dictionary/hashmap, with each letter as a key and the number of times it appears as the value.

2) Increment count for each letter as you go through the first word

3) After that, go through the 2nd word and for each letter, remove characters. Add a check for if false, return False, so that we know it's empty early.

4) If it gets to the end, the 2 words are anagrams; return true.
"""

def verify_anagram(s: str, t: str) -> bool:
    letter_dict = {}
    for letter in s:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    for letter in t:
        if letter not in letter_dict:
            return False
        letter_dict[letter] -= 1
    for letter in letter_dict:
        if letter_dict[letter] != 0:
            return False
    return True