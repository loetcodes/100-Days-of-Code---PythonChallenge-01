"""
Day 73 - Products of items in array

Source: Daily Coding Problem

Level: Hard

Task:
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

Example:
Given the following input, the function should return the expected outputs.
	Input: [10, 15, 3, 7] 
	Output: [120, 60, 40, 30, 24]

	Input: [3, 2, 1] 
	Output: [2, 3, 6]

Follow up: What if you can't use division?

"""
#!/usr/bin/python3

# Brute force approach using division. 
def products_list(arr):
	""" Computes the product of all other numbers in the list passed into the function with the exception of each position, using division to calculate.
	Returns a list.
	"""
	product = 1
	zero = 0
	result = []
	if arr == []: return []
	elif len(arr) == 1: return [0]

	for i in arr:
		if i != 0:
			product *= i
		elif i == 0:
			zero += 1
	
	if zero > 1:
		result = [0 for i in arr]
		return result
	elif zero == 1:
		for i in arr:
			if i == 0:
				result.append(product)
			else:
				result.append(0)
	elif zero == 0:
		result = [product // i for i in arr]
	return result


# Brute force approach where division is not used. Takes O(N^2)
def products_list2(arr):
	""" Computes the product of all other numbers in the list passed into the function with the exception of each position, without division. Returns a list.
	"""
	if arr == []:
		return []
	elif len(arr) == 1:
		return [0]
	else:
		return [product(arr[:i] + arr[i + 1:]) for i in range(len(arr))]

def product(arr):
	""" Calculates the product of items in a list.
	"""
	result = 1
	for i in arr:
		result *= i
	return result



# Optimized function that takes O(N) time and space
def products_list3(nums):
	""" Computes the prefix and suffix products for an item i in the 
	nums list. By prefix we mean compute the product up to the list value of i, including the i.
	Returns a list of product values for each item in the given array.
	""" 
	if nums == []: return []
	elif len(nums) == 1: return [0]

	prefix_products = []
	suffix_products = []
	result = []

	# Generate the prefix products
	for num in nums:
		if prefix_products:
			prefix_products.append(prefix_products[-1] * num)
		else:
			prefix_products.append(num)
	
	# Generate the suffix products
	for num in reversed(nums):
		if suffix_products:
			suffix_products.append(suffix_products[-1] * num)
		else:
			suffix_products.append(num)
	suffix_products = list(reversed(suffix_products))

	# Compute the final list result
	for i in range(len(nums)):
		if i == 0:
			result.append(suffix_products[1])
		elif i == len(nums) - 1:
			result.append(prefix_products[i - 1])
		else:
			result.append(prefix_products[i - 1] * suffix_products[i + 1])
	return result




if __name__ == "__main__":
	assert(products_list([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24])
	assert(products_list([3, 2, 1]) == [2, 3, 6])
	assert(products_list([1, 1, 0]) == [0, 0, 1])
	assert(products_list([0, 1]) == [1, 0])
	assert(products_list([1, 5, 10, 1]) == [50, 10, 5, 50])
	assert(products_list([5, 2, 10, 0]) == [0, 0, 0, 100])
	assert(products_list([10, 15, 3, 7]) == [315, 210, 1050, 450])
	assert(products_list([0, 5, 1, 10, 0]) == [0, 0, 0, 0, 0])
	assert(products_list([]) == [])
	assert(products_list([5]) == [0])
	print('Run 10 tests on product_list(arr) with 0 failures.')

	assert(products_list2([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24])
	assert(products_list2([3, 2, 1]) == [2, 3, 6])
	assert(products_list2([1, 1, 0]) == [0, 0, 1])
	assert(products_list2([0, 1]) == [1, 0])
	assert(products_list2([1, 5, 10, 1]) == [50, 10, 5, 50])
	assert(products_list2([5, 2, 10, 0]) == [0, 0, 0, 100])
	assert(products_list2([10, 15, 3, 7]) == [315, 210, 1050, 450])
	assert(products_list2([0, 5, 1, 10, 0]) == [0, 0, 0, 0, 0])
	assert(products_list2([]) == [])
	assert(products_list2([5]) == [0])
	print('Run 10 tests on product_list2(arr) with 0 failures.')

	assert(products_list3([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24])
	assert(products_list3([3, 2, 1]) == [2, 3, 6])
	assert(products_list3([1, 1, 0]) == [0, 0, 1])
	assert(products_list3([0, 1]) == [1, 0])
	assert(products_list3([1, 5, 10, 1]) == [50, 10, 5, 50])
	assert(products_list3([5, 2, 10, 0]) == [0, 0, 0, 100])
	assert(products_list3([10, 15, 3, 7]) == [315, 210, 1050, 450])
	assert(products_list3([0, 5, 1, 10, 0]) == [0, 0, 0, 0, 0])
	assert(products_list3([]) == [])
	assert(products_list3([5]) == [0])
	print('Run 10 tests on product_list3(arr) with 0 failures.')