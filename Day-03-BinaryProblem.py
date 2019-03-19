"""

Task 
Given a base-10 integer,n ,convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.

Input Format
A single integer,n .

Constraints
1 <= n <= 10**6

Output Format
Print a single base-10 integer denoting the maximum number of consecutive 1's in the binary representation of n.

Sample Input 1: 5
Sample Output 1: 1

Sample Input 2: 13
Sample Output 2: 2

Personal comments: Consider edge cases like the final binary being a 1 example in 439, binary is 110110111. Output should be 3.

"""

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
	n = int(input())
	binary_vals = []

	#populate binary list first
	while n > 0:
		rem = n % 2
		n = math.floor(n / 2)
		binary_vals.append(rem)
	binary_vals.reverse()

	#Counts consecutive 1s in binary value list
	curr_count = 0
	final_count = 0
	for val in range(len(binary_vals)):
		if binary_vals[val] == 1:
			curr_count += 1
		else:
			if curr_count > final_count:
				final_count = curr_count
			curr_count = 0
	if final_count < curr_count:
		final_count = curr_count
	print(final_count)