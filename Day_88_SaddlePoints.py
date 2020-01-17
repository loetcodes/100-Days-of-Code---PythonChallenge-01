"""
Day 88 - Saddle Points

Exercism

Detect saddle points in a matrix.

So say you have a matrix like so:

    1  2  3
  |---------
1 | 9  8  7
2 | 5  3  2     <--- saddle point at (2,1)
3 | 6  6  7
It has a saddle point at (2, 1).

It's called a "saddle point" because it is greater than or equal to every element in its row and less than or equal to every element in its column.

A matrix may have zero or more saddle points.

Your code should be able to provide the (possibly empty) list of all the saddle points for any given matrix.

Note that you may find other definitions of matrix saddle points online, but the tests for this exercise follow the above unambiguous definition.

Exception messages
Sometimes it is necessary to raise an exception. When you do this, you should include a meaningful error message to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. Not every exercise will require you to raise an exception, but for those that do, the tests will only pass if you include a message.
"""

#!/bin/python3

def saddle_points(matrix):
    ''' Returns saddle points in a list from a given matrix
    returns : list of points
    '''
    # If the matrix is empty or irregular return.
    if len(matrix) == 0:
        return []
    
    for dummy_row in matrix:
        if len(dummy_row) != len(matrix[0]):
            raise ValueError('irregular matrix has been passed')

    result = []
    col_count = len(matrix[0])

    # Compute the max for each row and min for each col
    max_rows = [max(row) for row in matrix]
    min_cols = [min([row[i] for row in matrix]) for i in range(col_count)]

    # Compute the saddle points by comparing to max row and min col
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val >= max_rows[i] and val <= min_cols[j]:
                result.append({'row' : i + 1, 'column' : j + 1})
    return result



if __name__ == "__main__":

    # matrix = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
    # saddle_points(matrix)

    # matrix = [[4, 5, 4], [3, 5, 5], [1, 5, 4]]
    # print(saddle_points(matrix))

    # matrix = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
    # saddle_points(matrix)

    # matrix = [[3, 2, 1], [0, 1], [2, 1, 0]]
    # print(saddle_points(matrix))