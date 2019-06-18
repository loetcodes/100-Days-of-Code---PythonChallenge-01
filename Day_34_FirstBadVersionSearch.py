"""

Day 34: First bad version using binary search

Leetcode

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 

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


