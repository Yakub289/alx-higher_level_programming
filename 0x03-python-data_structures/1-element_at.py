#!/usr/bin/python3

# Write a function that retrieves an element from a list like in C.

def element_at(my_list, idx):
    if idx < 0:
        return (None)
    elif idx > len(my_list):
        return (None)
    else:
        for list in range(len(my_list)):
            if idx == list:
                return (my_list[list])
