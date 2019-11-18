"""
Day 69 - Alphabet Rangoli

Hacker Rank - Easy

You are given an integer, N. Your task is to print an alphabet rangoli of size N. 
(Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter (in alphabetical order).

Input Format:
  Only one line of input containing N, the size of the rangoli.

Constraints:
  0 < N < 27

Output Format:
  Print the alphabet rangoli in the format explained above.

Sample Input:
  5
  
Sample Output:

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

"""
#!/usr/bin/python3

def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rangoli_chrs = alphabet[:size]
    string = ''
    width = (size - 1) * 4 + 1
    for i in range(size * 2 - 1):
        if i <= size - 1:
            letter_str = "-".join(list(rangoli_chrs[size - 1 - i: size]))
        else:
            letter_str = "-".join(list(rangoli_chrs[i - (size - 1): size]))
        reverse_str = letter_str[:0:-1]
        string = string + (reverse_str + letter_str).center(width, '-') + '\n'
    print(string)
  
if '__name__' == '__main__':
  n = int(input())
  print_rangoli(size)
  





