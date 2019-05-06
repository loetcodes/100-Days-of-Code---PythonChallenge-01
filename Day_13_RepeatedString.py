"""
Day 13 Repeated String - hackerrank

Lilah has a string,s, of lowercase English letters that she repeated infinitely many times.

Given an integer, n, find and print the number of letter a's in the first n letters of Lilah's infinite string.

For example, if the string s = 'abcac' and n=10, the substring we consider is 'abcacabcac', the first 10 characters of her infinite string. There are 4 occurrences of a in the substring.

repeatedString has the following parameter(s):
  s: a string to repeat
  n: the number of characters to consider

Input format:
The first line contains a single string,s . 
The second line contains an integer, n.

Constraints:
  1 <= |s| <= 100 
  1 <= n <= 10**12
  for 25% of the test cases, n <= 10**6

Output format:
Print a single integer denoting the number of letter a's in the first n letters of the infinite string created by repeating s infinitely many times.

Sample Input 0:
aba
10

Sample Output 0:
7

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    #Get no of times and remainder that s will repeat, multiply by num of a in s.
    a_num = s.count("a")
    repetitions = divmod(n, len(s))

    return (a_num * repetitions[0]) + s[:repetitions[1]].count("a")



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
