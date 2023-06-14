#!/usr/bin/python3

# Write a function that replaces all occurrences
# of an element by another in a new list.

def search_replace(my_list, search, replace):
    new_list = []
    for replace_list in range(len(my_list)):
        if my_list[replace_list] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[replace_list])
    return (new_list)
