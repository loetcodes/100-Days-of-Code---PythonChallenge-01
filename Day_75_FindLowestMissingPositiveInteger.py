"""
Day 75 - Find Lowest Missing Positive integer

Source: Daily Coding Problem

Level: Hard

Task:
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

Example:
Given the following input, the function should return the expected outputs.
	Input: [3, 4, -1, 1] 
	Output: 2

	Input: [1, 2, 0] 
	Output: 3

You can modify the input array in place



"""
#!/usr/bin/python3




	"""
Coding Problem 04

22-Nov-2019

Level: Hard

Task:
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.


Example:
Given the following input, the function should return the expected outputs.
	Input: [3, 4, -1, 1] 
	Output: 2

	Input: [1, 2, 0] 
	Output: 3

You can modify the input array in place

"""
#!/usr/bin/python3

# Linear time version - ideal solution
def findMissingPositive(nums):
	if not nums:
		return 1
	for i, num in enumerate(nums):
		while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
			v = nums[i]
			nums[i], nums[v - 1] = nums[v - 1], nums[i]
			if nums[i] == nums[v - 1]:
				break
	for i, num in enumerate(nums, 1):
		if num != i:
			return i
	return len(nums) + 1
	

# Second version, however runs in 0(N) in both time and space.
def findMissingInteger(arr):
	s = set(nums)
	i = 1
	while i in s:
		i += 1
	return i



if __name__ == "__main__":
	test_inputs = {
		"test_1" : ([3, 4, -1, 1], 2),
		"test_2" : ([1, 2, 0], 3),
		"test_3" : ([3, 4, -1, 2], 1),
		"test_4" : ([0, 0, 2, 3, 8], 1),
		"test_5" : ([-5, -1, -2, -3], 1),
		"test_6" : ([5, 8, 10, 12, 14], 1),
		"test_7" : ([0, 0, 0], 1)
	}

	for key in test_inputs:
		print("Testing input", test_inputs[key][0])
		assert test_inputs[key][1] == findMissingInteger(test_inputs[key][0]), "Returned incorrect output"
	print("Run tests ", len(test_inputs), " on findMissingInteger(arr) with 0 failures")

	for key in test_inputs:
		print("Testing input", test_inputs[key][0])
		assert test_inputs[key][1] == findMissingPositive(test_inputs[key][0]), "Returned incorrect output"
	print("Run tests ", len(test_inputs), " on findMissingPositive(arr) with 0 failures")