""""
HackerRank Level Easy

Consider a staircase of size :
   #
  ##
 ###
####

Observe that its base and height are both equal to n, and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size n.


Function Description:
Complete the staircase function in the editor below. It should print a staircase as described above. Staircase has the following parameter(s):

n: an integer


Input Format:
A single integer, n, denoting the size of the staircase.


Constraints:
0 <= n <= 100


Output Format:
Print a staircase of size using # symbols and spaces.
Note: The last line must have zero spaces in it.


Sample Input: 6
Sample Output:

     #
    ##
   ###
  ####
 #####
######


"""
#!/bin/python3
import math
import os
import random
import re
import sys

def staircase(n):
	case = ''
	for val in range(1, n + 1):
		case += (' ' * (n - val) + '#' * cal + '\n')
	print (case)


if __name__ == '__main__':
	n = int(input())
	staircase(n)
