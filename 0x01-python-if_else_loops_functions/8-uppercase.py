#!/usr/bin/python3

# Displaying alphabet in uppercase character.
# Using a function that checks for uppercase character.

def uppercase(str):
    for uppercase in str(97, 122):

        if ord(uppercase) >= 97 and ord(uppercase) <= 122:
            uppercase = chr(ord(uppercase) - 32)
            print("{}".format(uppercase), end="")
            print()
