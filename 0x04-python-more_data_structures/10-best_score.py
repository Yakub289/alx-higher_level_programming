#!/usr/bin/python3

# Write a function that returns a key with the biggest integer value.

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return (None)
    dict = 0
    for list in a_dictionary:
        if dict < a_dictionary[list]:
            dict = a_dictionary[list]
    for list in a_dictionary.keys():
        if a_dictionary[list] == dict:
            return (list)
