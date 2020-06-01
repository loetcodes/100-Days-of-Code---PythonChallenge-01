"""
Day 43 - Plus One

Leetcode

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
    Input: [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.

Example 2:
    Input: [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: The array represents the integer 4321.

"""

#!/bin/python3

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            return [1]
        last_val = digits[-1] + 1
        if last_val > 9:
            last_val = last_val % 10
            return self.plusOne(digits[:len(digits)-1]) + [last_val]

        return digits[:len(digits)-1] + [last_val]