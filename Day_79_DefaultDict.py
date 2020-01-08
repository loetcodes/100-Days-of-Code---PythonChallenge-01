"""
Day 79 - DefaultDict Tutorial

HackerRank

The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want. 

For example:
		from collections import defaultdict
		d = defaultdict(list)
		d['python'].append("awesome")
		d['something-else'].append("not relevant")
		d['python'].append("language")
		for i in d.items():
			print i

	This prints:
		('python', ['awesome', 'language'])
		('something-else', ['not relevant'])

In this challenge, you will be given 2 integers, n and m. There are  n words, which might repeat, in word group A. There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not. Print the indices of each occurrence of m in group A. If it does not appear, print -1.


Constraints:
	1 <= n <= 10000
	1 <= m <= 100
	1 <= length of each word in the input <= 100 
 

Input format:
	The first line contains integers, n and m separated by a space. 
	The next n lines contains the words belonging to group A. 
	The next m lines contains the words belonging to group B.


Output Format:
	Output m lines.
	The ith line should contain the 1 -indexed positions of the occurrences of the ith word separated by spaces.


Output  lines. 
The  line should contain the -indexed positions of the occurrences of the  word separated by spaces.

Sample Input:
	5 2
	a
	a
	b
	a
	b
	a
	b


Sample Output:
	1 2 4
	3 5


Explanation:
	'a' appeared  times in positions ,  and . 
	'b' appeared  times in positions  and . 
	In the sample problem, if 'c' also appeared in word group , you would print .

"""

#!/bin/python3

from collections import defaultdict

n, m = map(int, input().split(" "))
d = defaultdict(list)

for i in range(n):
    letter = input()
    d[letter].append(str(i + 1))

for i in range(m):
    letter = input()
    if d[letter]:
        print (" ".join(d[letter]))
    else:
        print(-1)


