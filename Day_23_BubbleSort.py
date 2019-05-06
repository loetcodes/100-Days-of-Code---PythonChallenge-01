"""
Day 23: Bubble Sort - Hackerrank


Task 
Given an array, a, of size n distinct elements, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following 3 lines:
	1. Array is sorted in numSwaps swaps.
	where numSwaps is the number of swaps that took place.
	2. First Element: firstElement
	where firstElement is the first element in the sorted array.
	3. Last Element: lastElement 
	where lastElement is the last element in the sorted array.

Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution.

Input Format:
The first line contains an integer, n, denoting the number of elements in array a. The second line contains n space-separated integers describing the respective values of a to a(n-1).

Constraints:
	2 <= n <= 600
	1 <= a(i) < 2 * 10**6, where 0 <= i <= n

Output Format:
Print the following three lines of output:
	Array is sorted in numSwaps swaps. 
	First Element: firstElement 
	Last Element: lastElement 

"""

#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

num_of_swaps = 0
for x in range(n):
    y = 1
    while (y <= n - 1):
        if a[y] < a[y - 1]:
            reassign = [a[y - 1], a[y]]
            a[y] = reassign[0]
            a[y - 1] = reassign[1]
            num_of_swaps += 1
        y += 1
        
print("Array is sorted in %d swaps." %num_of_swaps)
print("First Element:", a[0])
print("Last Element:", a[-1])

