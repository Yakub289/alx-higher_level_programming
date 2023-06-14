#!/usr/bin/python3

# Write a function that adds all unique integers in a list.

def uniq_add(my_list=[]):
    new_set = set(my_list)
    number = 0
    for element in new_set:
        number += element
    return (number)
