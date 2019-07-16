"""
Day 42 - First Unique Character in a String

Leetcode

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:
    s = "leetcode"
    return 0.

    s = "loveleetcode",
    return 2.

Note: You may assume the string contain only lowercase letters.

"""

#!/bin/python3

class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars_dict = {}
        for char in s:
            if char not in chars_dict:
                chars_dict[char] = 1
            else:
                chars_dict[char] += 1
                
        for i, char in enumerate(s):
            if chars_dict[char] == 1:
                return i
        return -1