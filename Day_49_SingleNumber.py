"""
Day 49 - Single Number

Leetcode

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
	Input: [2,2,1]
	Output: 1

Example 2:
	Input: [4,1,2,1,2]
	Output: 4

"""

#!/bin/python3

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_dict = {}
        for item in nums:
            if item not in nums_dict:
                nums_dict[item] = 1
            else:
                nums_dict.pop(item)
        return nums_dict.popitem()[0]