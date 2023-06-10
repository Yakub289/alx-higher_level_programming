#!/usr/bin/python3

# Write a function that finds all multiples of 2 in a list.

def divisible_by_2(my_list=[]):
    multiple = []
    for list in range(len(my_list)):
        if my_list[list] % 2 == 0:
            multiple.append(True)
        elif my_list[list] % 2 == 1:
            multiple.append(False)
    return (multiple)
