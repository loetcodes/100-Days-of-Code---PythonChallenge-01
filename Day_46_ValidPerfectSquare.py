"""
Day 46 - Valid Perfect Square

Leetcode

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
    Input: 16
    Output: true

Example 2:
    Input: 14
    Output: false

"""

#!/bin/python3

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start, end = 1, int(num / 2)
        while (start < end):
            mid = (start + end) // 2
            if (mid * mid == num):
                return True
            elif (mid * mid > num):
                end = mid
            else:
                start = mid + 1
        return start * start == num