#!/usr/bin/python3

# Write a function that prints the first x elements of a list and only integers

def safe_print_list_integers(my_list=[], x=0):
    access = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            access = access + 1
        except (ValueError, TypeError):
            pass
    print("")
    return (access)
