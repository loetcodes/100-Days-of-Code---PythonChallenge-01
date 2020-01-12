"""
Day 83 - Company Logo

HackerRank

Task:
	A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string s, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.
		Print the three most common characters along with their occurrence count. 
		Sort in descending order of occurrence count.
		If the occurrence count is the same, sort the characters in alphabetical order.
	
	For example, according to the conditions described above, GOOGLE would have it's logo with the letters, G, O, E.


Constraints:
	3 <= len(S) <= 10^4


Input Format:
	A single line of input containing the string S.


Output Format:
	Print the three most common characters along with their occurrence count each on a separate line. 
	Sort output in descending order of occurrence count. 
	If the occurrence count is the same, sort the characters in alphabetical order.


Sample Input:
	aabbbccde


Sample Output:
	b
	a
	c


Explanation:
	aabbbccde
	Here, b occurs 3 times. It is printed first.
	Both a and c occur 2 times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.
	Note: The string S has atleast 3 distinct characters.

"""

#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter, OrderedDict

if __name__ == '__main__':
	s = sorted(input())
	three_common = Counter(s).most_common(3)
	[print(a,b) for a,b in three_common]


	# Second solution involving counter and orderdict
	class OrderedCounter(Counter, OrderDict):
		pass
	[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]
