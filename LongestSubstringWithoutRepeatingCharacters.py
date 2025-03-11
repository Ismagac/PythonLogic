def length_of_longest_substring(s: str) -> int:
    char_index = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1

        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length

import unittest

class TestLongestSubstring(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(length_of_longest_substring("abcabcbb"), 3)
        self.assertEqual(length_of_longest_substring("bbbbb"), 1)
        self.assertEqual(length_of_longest_substring("pwwkew"), 3)
        self.assertEqual(length_of_longest_substring(""), 0)
        self.assertEqual(length_of_longest_substring("abcdef"), 6)
        self.assertEqual(length_of_longest_substring("abba"), 2)
        self.assertEqual(length_of_longest_substring("dvdf"), 3)

if __name__ == "__main__":
    unittest.main()
