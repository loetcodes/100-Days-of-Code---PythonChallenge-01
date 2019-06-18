"""
Day 33: Searching a rotated array for a value

Leetcode

Suppose an array sorted in ascending order is rotates at some pivot unknown to you before hand.

i.e. [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
	Input: nums = [4,5,6,7,0,1,2] target = 0
	Output: 4

Example 2:
	Input: nums = [4,5,6,7,0,1,2] target = 3
	Output: -1


"""

#!/bin/python3

class Solution:
	def search (self, nums:List[int], target: int):
		start = 0
		end = len(nums) - 1

		while start <= end:
			mid = (start + end) // 2

			if nums[mid] == target:
				return mid

			if nums[mid] <= nums[end]:
				if (target > nums[mid] and target <= nums[end]):
					start = mid + 1
				else:
					end = mid - 1
			elif (nums[mid] >= nums[start]):
				if (target < nums[mid] and target >= nums[start]):
					end = mid - 1
				else:
					start = mid + 1
		return -1


