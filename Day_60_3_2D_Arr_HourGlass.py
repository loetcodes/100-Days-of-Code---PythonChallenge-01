"""
Day 60 - 2D Array Hourglass sum

Hackerrank

Given a 6 X 6 2D Array, arr:

    1 1 1 0 0 0
    0 1 0 0 0 0
    1 1 1 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0

We define an hourglass in A to be a subset of values with indices falling in this pattern in arr's graphical representation:

    a b c
      d
    e f g

There are 16 hourglasses in arr, and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum.

For example, given the 2D array:

    -9 -9 -9  1 1 1 
     0 -9  0  4 3 2
    -9 -9 -9  1 2 3
     0  0  8  6 6 0
     0  0  0 -2 0 0
     0  0  1  2 4 0

We calculate the following 16 hourglass values:

    -63, -34, -9, 12, 
    -10, 0, 28, 23, 
    -27, -11, -2, 10, 
    9, 17, 25, 18

Our highest hourglass value is 28 from the hourglass:

    0 4 3
      1
    8 6 6

Input format:
    Each of the 6 lines of inputs arr[i] contains 6 space-separated integers arr[i][j].

Constraints:
    -9 <= arr[i][j] <= 9
    0 <= i,j <= 5

Output format:
    Print the largest (maximum) hourglass sum found in arr.

Sample Input:
    1 1 1 0 0 0
    0 1 0 0 0 0
    1 1 1 0 0 0
    0 0 2 4 4 0
    0 0 0 2 0 0
    0 0 1 2 4 0

Sample Output:
    19

Explanation:
    The hourglass with the maximum sum (19) is:
        2 4 4
          2
        1 2 4


"""
#!/bin/python3

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_sum = 0 - math.inf
    for i in range(4):
        for j in range(4):
            section_sum = sum(arr[i][j:j + 3]) + arr[i + 1][j + 1] + sum(arr[i + 2][j:j + 3])
            if section_sum > max_sum:
                max_sum = section_sum
    return max_sum



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
