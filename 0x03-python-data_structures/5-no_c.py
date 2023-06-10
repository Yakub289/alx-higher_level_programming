#!/usr/bin/python3

# Write a function that removes all characters c and C from a string.

def no_c(my_string):
    remove_str = ""
    for list in my_string:
        if list != "c" and list != "C":
            remove_str = remove_str + list
    return (remove_str)
