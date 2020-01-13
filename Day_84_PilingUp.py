"""
Day 84 - Piling Up

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

from collections import deque

tests = int(input())
for _ in range(tests):
    count = int(input())
    d = deque(map(int, input().split()))
    last_cube = d.popleft() if d[0] >= d[-1] else d.pop()
    while len(d) > 0:
        curr_cube = d.popleft() if d[0] >= d[-1] else d.pop()
        if curr_cube > last_cube:
            break
        else:
            last_cube = curr_cube
    print('Yes' if count - len(d) == count else 'No')



"""
Other implementation obtained from hackerrank not using deques but quite a nice one i must say.
"""
# for t in range(input()):
#     input()
#     lst = map(int, raw_input().split())
#     l = len(lst)
#     i = 0
#     while i < l - 1 and lst[i] >= lst[i+1]:
#         i += 1
#     while i < l - 1 and lst[i] <= lst[i+1]:
#         i += 1
#     print "Yes" if i == l - 1 else "No"