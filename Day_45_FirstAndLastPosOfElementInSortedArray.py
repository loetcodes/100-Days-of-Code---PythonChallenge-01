"""
Day 45 - Find First and Last Position of Element in Sorted Array

Leetcode

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

Example 2:
    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]

"""

#!/bin/python3

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                if (nums[left] == target and nums[right] == target):
                    return [left, right]
                if nums[left] != nums[mid]:
                    start = left
                    end = mid
                    while start <= end:
                        center = (start + end) // 2
                        if nums[center] == target and nums[center - 1] != target:
                            left = center
                            break
                        elif nums[center] < target:
                            start = center + 1
                        else:
                            end = center
                elif nums[right] != nums[mid]:
                    start = mid
                    end = right
                    while start < end:
                        center = (start + end) // 2
                        if nums[center] == target and nums[center + 1] != target:
                            right = center
                            break
                        elif nums[center] > target:
                            end = center
                        else:
                            start = center
            elif nums[mid] < target:
                left = mid
            else:
                right = mid-1
                    
        if nums[left] == nums[right] and nums[left] == target:
            return [left, right]
        if nums[right] == target and nums[left] != target:
            return [right, right]
        elif nums[left] == target and nums[right] != target:
            return [left, left]
        return [-1, -1]