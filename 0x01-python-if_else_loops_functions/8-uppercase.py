#!/usr/bin/python3

# Displaying alphabet in uppercase character.
# Using a function that checks for uppercase character.

def uppercase(str):
    for uppercase in str:

        if ord(uppercase) >= 97 and ord(uppercase) <= 122:
            uppercase = chr(ord(uppercase) - 32)
            print("{:c}".format(uppercase), end="")
            print("")
