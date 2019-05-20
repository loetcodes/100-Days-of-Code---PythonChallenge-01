"""
Day 29: Running Time

A prime is a natural number greater than 1 that has no positive divisors other than 1 and itself. Given a number, n, determine and print whether it's Prime or Not prime.

Note: If possible, try to come up with a  O(sqrt(n)) primality algorithm, or see what sort of optimizations you come up with for an O(n) algorithm. Be sure to check out the Editorial after submitting your code!

Input Format:
The first line contains an integer,T , the number of test cases. 
Each of the T subsequent lines contains an integer, n, to be tested for primality.

Constraints:
1 <= T <= 30
1 <= n <= 2 * 10^9

Output Format:
For each test case, print whether n is Prime or Not prime on a new line.

Sample Input:
 3
 12
 5
 7

Sample Output:
 Not prime
 Prime
 Prime


"""
#!/bin/python3

import math

def check_prime(num):
    val = int(math.sqrt(num))
    if (num % 2 == 0 and num != 2) or (num == 1):
        return 'Not prime'
    else:
        for i in range(3, val+1):
            if num % i == 0:
                return 'Not prime'
    return 'Prime'

N = int(input())
for i in range(N):
    num = int(input())
    print (check_prime(num))
    