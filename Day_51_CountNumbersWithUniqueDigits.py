"""
Day 51 - Count Numbers with Unique Digits

Leetcode

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
	Input: 2
	Output: 91 
	Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100,
	excluding 11,22,33,44,55,66,77,88,99


"""

#!/bin/python3

class Solution:
	def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        unique = 10
        prod = 1
        for i in range(1, n):
            prod = prod * (10 - i)
            unique += (9 * prod)
        return unique