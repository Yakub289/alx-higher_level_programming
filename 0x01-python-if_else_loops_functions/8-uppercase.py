#!/usr/bin/python3

# Displaying alphabet in change case.
# Using a function that checks for character case.

def uppercase(string):

    for uppercase in string:
        if ord(uppercase) <= 65 and ord(uppercase) >= 90:
            uppercase = chr(ord(uppercase) - 32)
        print("{}".format(uppercase), end="")
    print()
