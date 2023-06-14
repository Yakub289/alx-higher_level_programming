#!/usr/bin/python3

# Write a function that returns a new dictionary with all values multiply by 2.

def multiply_by_2(a_dictionary):
    multiply = {}
    for list in a_dictionary:
        multiply[list] = a_dictionary[list] * 2
    return (multiply)
