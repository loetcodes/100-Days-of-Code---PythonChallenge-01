"""
Day 87 - Find Anagrams

Exercism

Given a word and a list of possible anagrams, select the correct sublist.

Given "listen" and a list of candidates like "enlists" "google" "inlets" "banana" the program should return a list containing "inlets".


"""

#!/bin/python3

def find_anagrams(word, candidates):
    """ Returns a list of words that are anagrams for a given word.
    returns : list
    """
    letters = sorted(list(word.lower()))
    result = [item for item in candidates if item.lower() != word.lower() and sorted(list(item.lower())) == letters]
    return result
