"""
Day 100 - Spiral Matrix

Leetcode - Medium


Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


"""

# My solution
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Check if the matrix is empty or contains only 1 row
        if len(matrix) == 0:
            return []
        elif len(matrix) == 1:
            return matrix[0]
        
        #Check if matrix contains only 1 column
        if len(matrix[0]) <= 1:
            return [item[0] for item in matrix]
            
        matrix_i = [item for item in matrix]
        first_row, last_row = matrix_i[0], matrix_i[-1][::-1]
        first_col, last_col, mid_matrix = [], [], []
        if len(matrix_i) > 2:
            first_col, last_col = [], []
            for row in range(1, len(matrix_i) - 1):
                first_col.append(matrix_i[row][0])
                last_col.append(matrix_i[row][-1])
                if len(matrix_i[row]) > 2:
                    mid_matrix.append(list(matrix_i[row][1:-1]))
        result = first_row + last_col + last_row + first_col[::-1] + self.spiralOrder(mid_matrix)
        return result



class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return None  
        res=[]
        while matrix:
            res.extend([i for i in matrix.pop(0)])
            matrix=list(zip(*matrix))[::-1]
            print("Matrix is nw", matrix)
        return res

if __name__ == '__main__':