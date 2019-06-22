"""
Day 37 - Nested logic

HackerRank

Task 
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:
	1. If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0 .
	2. If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, the
		fine = 15 Hackos * (the number of days late).
	3. If the book is returned after the expected return month but still within the same calendar year as the expected return date, the
		fine = 500 Hackos * ( the number of months late).
	4. If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos.

Input Format:
The first line contains 3 space-separated integers denoting the respective day, month, and year  on which the book was actually returned. 
The second line contains 3 space-separated integers denoting the respective day, month, and year  on which the book was expected to be returned (due date).

Constraints:
	1 <= D <= 31
	1 <= M <= 12
	1 <= Y <= 3000
It is guaranteed that the dates will be valid Gregorian calendar dates.

Output Format:
Print a single integer denoting the library fine for the book received as input.

Sample Input:
9 6 2015
6 6 2015

Sample Output:
45

Explanation:
Given the following return dates: 
Actual:  D=9, M=6, Y=2015
Expected: D=6, M=6, Y=2015

Because Y1 = Y2, we know it is less than a year late. 
Because M1 = M2, we know it's less than a month late. 
Because D1 > D2, we know that it was returned late (but still within the same month and year).

Per the library's fee structure, we know that our fine will be
	15 Hackos * (#days late) . We then print the result as our output, which is 45


Test cases:
	"31 8 2004"
	"20 1 2004" 
	"3500"

	"31 12 2009"
	"1 1 2010"
	"0"

"""

#!/bin/python3

if __name__ == '__main__':
	returned = list(map(int, input().split()))
	expected = list(map(int, input().split()))

	day_fine = 15
	month_fine = 500
	year_fine = 10000
	fine = 0

	if returned[2] > expected[2]:
		fine = year_fine
	elif returned[2] == expected[2]:
		if returned[1] > expected[1]:
			fine = month_fine * (returned[1] - expected[1])
		elif returned[0] > expected[0]:
			fine = day_fine * (returned[0] - expected[0])
	print(fine)




