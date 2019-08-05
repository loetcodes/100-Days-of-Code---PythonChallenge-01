"""
Day 50 - Find Minimum In Rotated Sorted Array With Duplicates

Leetcode

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:
    Input: [1,3,5]
    Output: 1

Example 2:
    Input: [2,2,2,0,1]
    Output: 0

Note:
This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? 
How and why?


"""

#!/bin/python3

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return min(nums)
        left = 0
        right = len(nums)
        mid = (left + right) // 2
        if nums[mid - 1] > nums[mid]:
            return  nums[mid]
        else:
            return min(self.findMin(nums[left:mid]), self.findMin(nums[mid:right]))