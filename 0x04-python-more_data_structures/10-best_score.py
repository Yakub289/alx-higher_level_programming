#!/usr/bin/python3

# Write a function that returns a key with the biggest integer value.

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return (None)
    set = 0
    for list in a_dictionary:
        if set < a_dictionary[list]:
            set = a_dictionary[list]
    for list in a_dictionary.keys():
        if a_dictionary[list] == set:
            return (list)
