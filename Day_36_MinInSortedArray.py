"""

Day 36: Find minimum in Rotated Sorted Array using binary search


Leetcode

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.
You may assume no duplicate exists in the array.

Sample 1:
	Input: [3,4,5,1,2] 
	Output: 1

Sample 2:
	Input: [4,5,6,7,0,1,2]
	Output: 0


"""

#!/bin/python3

class Solution:
    def findMin(self, nums: List[int]) -> int:
#         if len(nums) < 2:
#             return nums[0]
        
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[right]