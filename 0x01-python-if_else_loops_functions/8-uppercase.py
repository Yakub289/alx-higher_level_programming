#!/usr/bin/python3

# Displaying alphabet in uppercase character.
# Using a function that checks for uppercase character.

def uppercase(str):

    for uppercase in range(65, 90):
        if ord(uppercase) >= 97 and ord(uppercase) <= 122:
            uppercase = chr(ord(uppercase) - 32)
        print("{}".format(uppercase), end="")
    print("")
