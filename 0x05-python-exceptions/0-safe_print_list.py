#!/usr/bin/python3

# Write a function that prints x elements of a list.
# my_list can contain any type (integer, string, etc.)
# All elements must be printed on the same line followed by a new line.
# x represents the number of elements to print
# x can be bigger than the length of my_list
# Returns the real number of elements printed
# You have to use try: / except:

def safe_print_list(my_list=[], x=0):
    digit = 0
    if isinstance(my_list, list) and isinstance(x, int):
        for numbers in range(x):
            try:
                print("{}".format(my_list[numbers]), end="\n")
            except IndexError:
                pass
            else:
                digit += 1
    print("\n")
    return (digit)
