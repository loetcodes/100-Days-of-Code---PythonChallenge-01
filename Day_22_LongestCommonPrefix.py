"""
Day 22: Longest Common Prefix  

source: Leetcode


Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
"""


class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ""
        if len(strs) > 0:
            benchmark = strs[0]
            for s in range(len(benchmark)):
                a = benchmark[s]
                for val in strs:
                    try:
                        if val[s] != a:
                            return prefix
                    except:
                        return prefix
                prefix += a
        return prefix

def main():
	test = Solution()
	test_cases = {"Input 1" : (["flower","flow","flight"], "fl"), "Input 2" : (["dog","racecar","car"], ""), "Input 3": (["blowtorch", "blow", "blowfish"], "blow"), "input 4": ([], "")}

	error = False
	for key, value in test_cases.items():
		print("Running test case: %s on %s" %(key, value[0]))
		x = test.longestCommonPrefix(value[0])
		if x != value[1]:
			print("Expected: %s \nObtained: %s" %(value[1], x))
			error = True

	if not error:
		print("Passed all testcases")

if __name__ == '__main__':
	main()