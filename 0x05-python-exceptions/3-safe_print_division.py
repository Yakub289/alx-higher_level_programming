#!/usr/bin/python3

# Write a function that divides 2 integers and prints the result.

def safe_print_division(a, b):
    try:
        divide_numbers = a / b
    except (ZeroDivisionError):
        divide_numbers = None
    finally:
        print("Inside result: {:d}".format(divide_numbers))
    return divide_numbers
