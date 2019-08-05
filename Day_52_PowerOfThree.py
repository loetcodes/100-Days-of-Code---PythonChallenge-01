"""
Day 52 - Power of Three

Leetcode

Given an integer, write a function to determine if it is a power of three.

Example 1:
    Input: 27
    Output: true

Example 2:
    Input: 0
    Output: false

Example 3:
    Input: 9
    Output: true

Example 4:
    Input: 45
    Output: false

Follow up:
Could you do it without using any loop / recursion?

"""

#!/bin/python3

from math import log

# Two versions of the solution. One that uses loops and another that uses log
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # solution without loop or recursion
        if n < 1:
            return False
        while n > 1:
            if n % 3 == 0:
                n = n // 3
            else:
                return False
        return True 


class Solution2:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        power = round(log(n, 3))
        return (3 ** power) == n