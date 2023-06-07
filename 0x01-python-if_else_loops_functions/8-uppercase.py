#!/usr/bin/python3

# Displaying alphabet in change case.
# Using a function that checks for character case.

def uppercase(string):
    for char in string:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()
