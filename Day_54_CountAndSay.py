"""

Day 54 - Count And Say

Leetcode

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string. 

"""
#!/bin/python3
class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for i in range(1, n):
            current_seq = result
            character = current_seq[0]
            count = 0
            temp_result = ""
            for char in current_seq:
                if char == character:
                    count += 1
                else:
                    temp_result += (str(count) + character)
                    count = 1
                character = char
            if count > 0:
                result = temp_result + (str(count) + character)
        return result
