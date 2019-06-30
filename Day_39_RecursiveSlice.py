"""
Day 39 - Recursive Slice

Write a function that recursively slices a list without using the built in python slice method.

Write a function slice(my_list,first,last) that takes as input a list my_list and two non-negative integer indices first and last satisfying 0 ≤ first ≤ last ≤n where n is the length of my_list. slice should return the corresponding Python list slice my_list[first:last]. For example, slice([’a’,’b’,’c’,’d’,’e’], 2, 4]) should return [’c’,’d’].
Important: Your solution should not use Python's built-in slice operator : anywhere in its implementation. Instead use the method pop to remove one element from the input list during each recursive call. 
(You may mutate the input list to simplify your solution.)

"""

#!/bin/python3

def slice(my_list, first, last):
	"""
    Takes a list, a starting index, an ending index and uses recursion to return a new list from the start to the end index.
    returns a new slice list
    """
    if my_list == []:
        return []
    else:
        if first == last - 1:
            return [my_list[last-1]]
        elif last > first:
            start = [my_list.pop(first)]
            return start + slice(my_list, first, last - 1)
        else:
            return []
        

def test_slice():
    """
    Some test cases for slice
    """
    print ("Computed:", slice(['a', 'b', 'c', 'd', 'e'], 2, 4) , "Expected: ", ['c', 'd'],)
    print ("Computed:", slice(['a', 'b', 'c', 'd', 'e'], 1, 4) , "Expected: ", ['b','c', 'd'])
    print ("Computed:", slice([], 0, 0), "Expected: ", [])
    print ("Computed:", slice([1], 0, 0), "Expected: ", [])
    print ("Computed:", slice([1], 0, 1), "Expected: ", [1])
    print ("Computed:", slice([], 0, 0), "Expected: ", [])
    print ("Computed:", slice([1, 2, 3], 0, 3), "Expected: ", [1, 2, 3])
    print ("Computed:", slice([1, 2, 3], 1, 2), "Expected: ", [2])    

    
if __name__ == '__main__':
    	test_slice()


