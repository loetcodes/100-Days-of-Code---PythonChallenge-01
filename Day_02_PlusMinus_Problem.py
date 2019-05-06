"""

 Adapted from Hackerrank

 Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.

  Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10**4 are acceptable.

  For example, given the array  arr=[1,1,0,-1,-1] there are  elements, two positive, two negative and one zero. Their ratios would be 2/5 = 0.400000, 2/5 = 0.400000 and 1/5 = 0.200000. They should be print as:
  0.40000
  0.40000
  0.20000

  Function description
  Complete the plusMinus function in the editor below. It should print out the ratio of positive, negative and zero items in the array, each on a separate line rounded to six decimals.

  Input Format:  for n spaced integers, they are written as arr(arr[0],arr[1],arr[2]....arr[n-1])

  Output Format
  You must print the following  lines:
  1. A decimal representing of the fraction of positive numbers in the array compared to its size.
  2. A decimal representing of the fraction of negative numbers in the array compared to its size.
  3. A decimal representing of the fraction of zeros in the array compared to its size.

  Sample Input 1

  6
  -4 3 -9 0 4 1

  Sample Input 2
  7
  1 -2 -7 9 1 -8 -5



"""


#!/bin/python3




import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    count_values = {"-":0, "+":0, "0":0}
    total = len(arr)
    for val in arr:
        if val < 0:
            count_values["-"] += 1
        elif val == 0:
            count_values["0"] += 1
        elif val > 0:
            count_values["+"] += 1

    print ('{:.6f}'.format(count_values["+"] / total))
    print ('{:.6f}'.format(count_values["-"] / total))
    print ('{:.6f}'.format(count_values["0"] / total))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))


    plusMinus(arr)
