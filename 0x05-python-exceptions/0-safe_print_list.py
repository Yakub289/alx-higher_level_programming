#!/usr/bin/python3

# Write a function that prints x elements of a list.

def safe_print_list(my_list=[], x=0):
    number = 0
    for digits in range(x):
        try:
            print(f"{my_list[digits]}", end="")
            number += 1
        except IndexError:
            break
        else:
            print("")
        return (number)
