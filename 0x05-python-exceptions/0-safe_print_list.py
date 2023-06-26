#!/usr/bin/python3

# Write a function that prints x elements of a list.
# my_list can contain any type (integer, string, etc.)
# All elements must be printed on the same line followed by a new line.

def safe_print_list(my_list=[], x=0):
    number = 0
    for digits in range(x):
        try:
            print(f"{my_list[digits]}", end="")
            number += 1
        except IndexError:
            break
    print("")
    return(number)
