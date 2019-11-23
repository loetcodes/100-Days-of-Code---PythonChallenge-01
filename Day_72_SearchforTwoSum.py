"""
Day 72 - Search for the two values that give sum K

Level: Easy

Task:
Given a list of numbers and a number K.
Return whether any two numbers from the list that add up to K.

Example:
Given [10, 15, 3, 7] and K = 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

"""
#!/usr/bin/python3

# Brute force approach. 
def checklist_one(arr, k):
	""" Checks whether two values sum up to the value k.
	Loops through the list, one index at a time,
	checking the remainder index positions after.
	Returns True or False.
	"""
	for index, x in enumerate(arr):
		sub_arr = arr[index + 1:]
		for y in sub_arr:
			if x + y == k:
				return True
	return False

# Memoization approach
def checklist_two(arr, k):
	""" Loops through an arr, creating a dictionary to store
	matching values that sum up to the passed value k.
	Returns True or False 
	"""
	memo = {}
	for value in arr:
		if value in memo:
			return True
		else:
			memo[k - value] = value
	return False


if __name__ == "__main__":
	assert(checklist_one([10, 15, 3, 7], 17) == True)
	assert(checklist_one([10, 15, 3, 7], 10) == True)
	assert(checklist_one([10, 15, 3, 7], 18) == True)
	assert(checklist_one([10, 15, 3, 7], 0) == False)
	assert(checklist_one([0, 15, 3, 7], 7) == True)
	assert(checklist_one([0, 15, 3, 7], 3) == True)
	print('Run 6 tests with 0 failures.')