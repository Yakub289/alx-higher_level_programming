#!/usr/bin/python3

# Write a function that deletes keys with a specific value in a dictionary.

def complex_delete(a_dictionary, value):
    for x in list(a_dictionary):
        if a_dictionary[x] == value:
            del a_dictionary[x]
    return (a_dictionary)
