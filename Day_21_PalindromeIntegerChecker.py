"""
Day 21 Palindrome Integer Checker  - Leetcode


Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Could you solve it without converting the integer to a string?


"""
import sys
import io



class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0  and (x == 0 or x % 10 != 0):
            original_num = x
            reversed_num = 0
            while original_num > reversed_num:
                new_value = divmod(original_num, 10)
                reversed_num = reversed_num * 10 + new_value[1]
                original_num = new_value[0] 
            if (original_num == reversed_num) or (original_num == reversed_num // 10):
                return True        
        return False



def main():
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            x = int(line);
            
            ret = Solution().isPalindrome(x)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()