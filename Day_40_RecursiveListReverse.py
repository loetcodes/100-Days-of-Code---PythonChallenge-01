"""
Day 40 - Recursive list reverse

Write a function list_reverse(my_list) that takes a list and returns a new list whose elements appear in reversed order. For example, list_reverse([2,3,1]) should return [1,3,2]. Do not use the reverse() method for lists.

"""

#!/bin/python3

def list_reverse(my_list):
    """
    Takes a list and reverses the list without using the reverse method.
    Returns a reversed list
    """
    if len(my_list) <= 1:
        return my_list
    else:
        n = [my_list[-1]]
        return n + list_reverse(my_list[:-1])



def test_list_reverse():
    """
    Some test cases for list reverse
    """
    print ("Computed:", list_reverse([1,2,3,4]), "Expected: ", [4, 3, 2, 1])
    print ("Computed:", list_reverse([0,2,2,1]), "Expected: ",[1, 2, 2, 0])
    print ("Computed:", list_reverse([]), "Expected: ", [])
    print ("Computed:", list_reverse([4]), "Expected: ", [4])
    print ("Computed:", list_reverse(['i', 'd', 'g', 'a', 'f']), "Expected: ", ['f', 'a', 'g', 'd', 'a'])


if __name__ == '__main__':
        test_list_reverse()