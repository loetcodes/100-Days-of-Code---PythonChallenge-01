"""
Day 32: Square root using binary search algorithm

Leetcode

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
	Input: 4
	Output: 2

Example 2:
	Input: 8
	Output: 2
	Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

"""

#!/bin/python3

class Solution:
	def mySqrt(self, x:int):
		""" Compute half the value as it can never be more than half.
		Check the square value.
		Return the previous number to account for truncating
		"""
		if(x == 0 or x == 1):
			return x
		start = 1
		val = 1
		while val <= x:
			start += 1
			val = start * start
		return start - 1
		

