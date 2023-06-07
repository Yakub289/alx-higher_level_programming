#!/usr/bin/python3

# Displaying alphabet in change case.
# Using a function that checks for character case.

def uppercase(str):

    for uppercase in range(65, 90):
        if ord(uppercase) <= 97 and ord(uppercase) >= 122:
            uppercase = chr(ord(uppercase) - 32)
        print("{}".format(uppercase), end="")
    print("Z")
