"""
Day 70 - Merge The Tools

Hacker Rank - Medium

Consider the following:
  A string, s, of length n where s = c(subscript0)c(subscript1)c(subscript2).....c(subscript n-1).
  An integer, k, where k is a factor of n.
  
We can split s into n / k subsegments where each subsegment, t(i), consists of a contiguous block of k characters in s. Then, use each t(i) to create string u(i) such that:
  The characters in u(i) are a subsequence of the characters in t(i).
  Any repeat occurrence of a character is removed from the string such that each character in u(i) occurs exactly once. In other words, if the character at some index j in t(i) occurs at a previous index < j in t(i), then do not include the character in string u(i).
  
Given s and k, print n / k lines where each line i denotes string u(i).

Input Format:
  The first line contains a single string denoting s.
  The second line contains an integer, k, denoting the length of each subsegment.

Constraints:
  1 <= n <= 10 ^ 4, where n is the length of s.
  1 <= k <= n
  It is guaranteed that n is a multiple of k.
  
Output Format:
  Print n / k lines where each line i contains string u(i).

Sample Input:
  AABCAAADA
  3  
  
Sample Output:
  AB
  CA
  AD
  
Explanation:
  String s is split into n / k = 9 / 3 = 3 equal parts of length k = 3. We convert each t(i) to u(i) by removing any subsequent occurrences non-distinct characters in t(i):
    1. t(0) = "AAB" - u(0) = "AB"
    2. t(1) = "CAA" - u(1) = "CA"
    3. t(2) = "ADA" - u(2) = "AD"

We then print each u(i) on a new line.

"""


#!/usr/bin/python3

def merge_the_tools(string, k):
    # your code goes here
    s = iter(string)
    for i in zip(*([s] * k)):
        seq_dict = dict()
        set_seq = "".join([seq_dict.setdefault(c, c) for c in i if c not in seq_dict])
        print (set_seq)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
