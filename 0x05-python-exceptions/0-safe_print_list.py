#!/usr/bin/python3

# Write a function that prints x elements of a list.

def safe_print_list(my_list=[], x=0):
    number = 0
    for element in range(x):
        try:
            print(my_list[element], end="")
        except IndexError:
            break
        else:
            number = number + 1
    print()
    return number
