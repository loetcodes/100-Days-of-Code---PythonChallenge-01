"""
Day 99 - Absolute Sort Value


Given an array of integers arr, write a function absSort(arr), that sorts the array according to the absolute values of the numbers in arr. If two numbers have the same absolute value, sort them according to sign, where the negative numbers come before the positive numbers.

Examples:

input:  arr = [2, -7, -2, -2, 0]
output: [0, -2, -2, 2, -7]
Constraints:

[time limit] 5000ms
[input] array.integer arr
0 ≤ arr.length ≤ 10
[output] array.integer
"""

# Using a customs sort
def compare(a, b):
  if abs(a) < abs(b): return -1
  if abs(a) > abs(b): return 1
  if a < b: return -1
  if a > b: return 1
  return 0

def absSort(arr):
  arr.sort(cmp= compare)
  return arr


if __name__ == '__main__':
  assert absSort([-8, 8,-8, 5, 0, -2, 2]) == [0, -2, 2, 5, -8,-8, 8]
  assert absSort([-1, -1, 1, 0, -10]) == [0, -1, -1, 1, 10]
  assert absSort([0, 1, 0, -1]) == [0, 0, -1, 1]