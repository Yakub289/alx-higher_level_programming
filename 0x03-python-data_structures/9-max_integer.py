#!/usr/bin/python3

# Write a function that finds the biggest integer of a list.

def max_integer(my_list=[]):
    if my_list == []:
        return (None)
    else:
        biggest = my_list[0]
        for list in range(len(my_list)):
            if biggest < my_list[list]:
                biggest = my_list[list]
        return (biggest)
