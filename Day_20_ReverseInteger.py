"""
Day 20: Reverse Integer
Source: leetcode


Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
  Input: 123
  Output: 321

Example 2:
  Input: -123
  Output: -321

Example 3:
  Input: 120
  Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""

#!/bin/python3

class Solution:
    def reverse(self, x: int) -> int:
        digits = abs(x)
        # Gets rid of try and except for 0 value input
        sign = x // max(1, digits)
        reversed_digits = int(str(digits)[::-1])
        if reversed_digits < (2**31):
            return sign * reversed_digits
        else:
            return 0