#!/usr/bin/python3

# Write a function that replaces an element in a list
#  at a specific position without modifying the original list (like in C).

def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list)
    else:
        new_list = []
        for list in range(len(my_list)):
            if list != idx:
                new_list.append(my_list[list])
            else:
                new_list.append(element)
        return (new_list)
