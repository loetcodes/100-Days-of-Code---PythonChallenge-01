"""

Day 31 Matrix formatting

Exercism

Problem statement:
Given a string representing a matrix of numbers, return the rows and columns of that matrix.

So given a string with embedded newlines like:

9 8 7
5 3 2
6 6 7
representing this matrix:

    1  2  3
  |---------
1 | 9  8  7
2 | 5  3  2
3 | 6  6  7
your code should be able to spit out:

A list of the rows, reading each row left-to-right while moving top-to-bottom across the rows,
A list of the columns, reading each column top-to-bottom while moving from left-to-right.
The rows for our example matrix:

9, 8, 7
5, 3, 2
6, 6, 7
And its columns:

9, 5, 6
8, 3, 6
7, 2, 7

"""
#!/bin/python3

class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string.split('\n')
        self.rows = [[int(s) for s in n.split(" ")] for n in self.matrix_string]
        self.columns = [list(self.rows[y][x] for y in range(len(self.rows))) for x in range(len(self.rows[0]))]

    def row(self, index):
    	return self.rows[index - 1]

    def column(self, index):
        return self.columns[index - 1]


def main():
	matrix = Matrix("1")
	assert (matrix.row(1) == [1])

	matrix = Matrix("1 2\n3 4")
	assert (matrix.row(2) == [3, 4])

	matrix = Matrix("1 2\n10 20")
	assert (matrix.row(2) == [10, 20])

	matrix = Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6")
	assert (matrix.column(3) == [3, 6, 9, 6])

	matrix = Matrix("89 1903 3\n18 3 1\n9 4 800")
	assert (matrix.column(2) == [1903, 3, 4])

	print("Ran all tests")


if __name__ == '__main__':
	main()