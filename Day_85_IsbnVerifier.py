"""
Day 85 - ISBN Verifier

Exercism

Backstory:
The [ISBN-10 verification process](https://en.wikipedia.org/wiki/International_Standard_Book_Number) is used to validate book identification numbers. These normally contain dashes and look like: `3-598-21508-8`

ISBN:
The ISBN-10 format is 9 digits (0 to 9) plus one check character (either a digit or an X only). In the case the check character is an X, this represents the value '10'. These may be communicated with or without hyphens, and can be checked for their validity by the following formula:

```
(x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) mod 11 == 0
```

If the result is 0, then it is a valid ISBN-10, otherwise it is invalid.


Example:
Let's take the ISBN-10 `3-598-21508-8`. We plug it in to the formula, and get:
```
(3 * 10 + 5 * 9 + 9 * 8 + 8 * 7 + 2 * 6 + 1 * 5 + 5 * 4 + 0 * 3 + 8 * 2 + 8 * 1) mod 11 == 0
```
Since the result is 0, this proves that our ISBN is valid.


Task:
Given a string the program should check if the provided string is a valid ISBN-10.
Putting this into place requires some thinking about preprocessing/parsing of the string prior to calculating the check digit for the ISBN.

The program should be able to verify ISBN-10 both with and without separating dashes.

"""

#!/bin/python3

def is_valid(isbn):
    """ Given a string, verify if the string is a valid isbn number or not.
    Input: str
    Output: boolean.
    """
    if (isbn == '' or not ((48 <= ord(isbn[-1]) <= 57) or ord(isbn[-1]) == 88)):
        return False
    
    y = 10 if ord(isbn[-1]) == 88 else isbn[-1]
    numbers = [int(i) for i in isbn[:-1] if 48 <= ord(i) <= 57] + [int(y)]
    if len(numbers) != 10:
        return False
    result = 0
    for index, value in enumerate(numbers):
        result += value * (10 - index)
    return result % 11 == 0





def verifier_tests():
    self.assertIs(is_valid("3-598-21508-8"), True)
	self.assertIs(is_valid("3-598-21508-9"), False)
	self.assertIs(is_valid("3-598-21507-X"), True)
	self.assertIs(is_valid("3-598-21507-A"), False)
	self.assertIs(is_valid("3-598-P1581-X"), False)
	self.assertIs(is_valid("3-598-2X507-9"), False)
	self.assertIs(is_valid("3598215088"), True)
	self.assertIs(is_valid("359821507X"), True)
	self.assertIs(is_valid("359821507"), False)
	self.assertIs(is_valid("3598215078X"), False)
	self.assertIs(is_valid("00"), False)
	self.assertIs(is_valid("3-598-21507"), False)
	self.assertIs(is_valid("3-598-21515-X"), False)
	self.assertIs(is_valid(""), False)
	self.assertIs(is_valid("134456729"), False)
	self.assertIs(is_valid("3132P34035"), False)
	self.assertIs(is_valid("98245726788"), False)



if __name__ == '__main__':
	verifier_tests()