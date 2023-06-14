#!/usr/bin/python3

# Write a function that prints a dictionary by ordered keys.

def print_sorted_dictionary(a_dictionary):
    for items in sorted(a_dictionary):
        print("{:s}: {}".format(items, a_dictionary[items]))
