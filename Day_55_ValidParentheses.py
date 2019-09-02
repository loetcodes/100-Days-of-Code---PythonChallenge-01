"""
Day 55 Valid Parentheses

Leetcode

Task:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
  Open brackets must be closed by the same type of brackets.
  Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:
  Input: "()"
  Output: true
  
Example 2:
  Input: "()[]{}"
  Output: true

Example 3:
  Input: "(]"
  Output: false

Example 4:
  Input: "([)]"
  Output: false

Example 5:
  Input: "{[]}"
  Output: true

"""
#!/bin/python3

class Solution:
    def isValid(self, s: str) -> bool:
        brackets_dict = {"(" : ")", "{" : "}", "[" : "]"}
        stack = []
        for bracket in s:
            if bracket in brackets_dict:
                stack.append(bracket)
            else:
                if stack:
                    top = stack.pop()
                    if brackets_dict[top] != bracket:
                        return False
                else:
                    return False
        if stack:
            return False
        return True
