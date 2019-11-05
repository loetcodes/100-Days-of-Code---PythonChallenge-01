"""
Day 62  2 - Swap case 
Hacker rank (Easy)

Task:
You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2

Input Format:
  A single line containing a string .

Constraints:
  0 <= len(S) <= 1000

Output Format
  Print the modified string S.

Sample Input 0:
  HackerRank.com presents "Pythonist 2".

Sample Output 0:
  hACKERrANK.COM PRESENTS "pYTHONIST 2".
  
"""

#!/bin/python3
def swap_case(s):
  return s.swapcase()
  
  # alternative solution
  # return "".join([i.lower() if i.isupper() else i.upper() for i in s])
  
if __name__ == "__main__":
  s = input()
  result = swap_case(s)
  print(result)
