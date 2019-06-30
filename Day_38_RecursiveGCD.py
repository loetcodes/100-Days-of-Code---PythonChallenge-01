"""
Day 38 - Recursive GCD

Write a function gcd(num1,num2) that takes two non-negative integers and computes the greatest common divisor ofnum1 and num2. 
To simplify the problem, you may assume that the greatest common divisor of zero and any non-negative integer is the integer itself. For an extra challenge, your programs should only use subtraction. 

Used the 'Euclid's Algorithm'

"""

#!/bin/python3

def gcd(num1, num2):
    """
    Takes non-negative integers num1 and num2 and
    returns the greatest common divisor of these numbers
    """
    if num2 > num1:
        return gcd(num2, num1)
    else:
        if num2 == 0:
            return num1
        else:
            return gcd(num1 - num2, num2)

def test_gcd():
    """
    Some test cases for gcd
    """
    print ("Computed:", gcd(4, 16), "Expected: ", 4)
    print ("Computed:", gcd(0, 16), "Expected: ", 16)
    print ("Computed:", gcd(1, 0), "Expected: ", 1)
    print ("Computed:", gcd(0, 0), "Expected: ", 0)
    print ("Computed:", gcd(14, 7), "Expected: ", 7)
    print ("Computed:", gcd(0, 0), "Expected: 0")
    print ("Computed:", gcd(3, 0), "Expected: 3")
    print ("Computed:", gcd(0, 2), "Expected: 2")
    print ("Computed:", gcd(12, 4), "Expected: 4")
    print ("Computed:", gcd(24, 18), "Expected: 6")

    
if __name__ == '__main__':
        test_gcd()