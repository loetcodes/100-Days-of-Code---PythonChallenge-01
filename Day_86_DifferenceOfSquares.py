"""
Day 86 - Difference of Squares

Exercism

Find the difference between the square of the sum and the sum of the squares of the first N natural numbers.

Example:
The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)² = 55² = 3025.
The sum of the squares of the first ten natural numbers is 1² + 2² + ... + 10² = 385.

Hence the difference between the square of the sum of the first ten natural numbers and the sum of the squares of the first ten natural numbers is 3025 - 385 = 2640.

You are not expected to discover an efficient solution to this yourself from first principles; research is allowed, indeed, encouraged. Finding the best algorithm for the problem is a key skill in software engineering.



"""

#!/bin/python3

def square_of_sum(number):
    """ Calculates the square of the sum of n natural numbers from 1 to number. Uses a list comprehension to calculate. Alternative would be to use the (n + 1) * (n / 2)
    parameter : int
    return : int
    """
    total = sum([i for i in range(1, number + 1)])
    return total * total


def sum_of_squares(number):
    """ Calculates the sum of the squares of numbers from 1 to number given.
    parameter: int
    return : int
    """
    return sum([i*i for i in range(1, number + 1)])


def difference_of_squares(number):
    """ Calculates the difference of the square of the sum and the sum of squares of natural numbers from 1 to number.
    parameter: int
    return : int
    """
    return square_of_sum(number) - sum_of_squares(number)