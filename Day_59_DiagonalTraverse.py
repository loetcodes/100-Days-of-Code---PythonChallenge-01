"""
Day 59 - Diagonal Traverse

Leetcode


Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 
Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:
diagonally moves from up down up down

Note:

The total number of elements of the given matrix will not exceed 10,000.

"""
#!/bin/python3

class Solution:
	def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == [] or matrix[0] == []:
            return None
        result = []
        rows = len(matrix)
        columns = len(matrix[0])
        
        for l in range(rows + columns - 1):
            temp_value = []
            for i in range(max(0, l - columns + 1), min(rows, l + 1)):
                temp_value.append(matrix[i][l - i])
            if l % 2 == 0:
                temp_value.reverse()
            result += temp_value
        return result 