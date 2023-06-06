#!/usr/bin/python3

# Displaying alphabet in uppercase character.
# Using a function that checks for uppercase character.
def uppercase(str):
    for uppercase in range (65, 90):
        if uppercase <= 65 and uppercase >=90:
            print("{:c}".format(uppercase), end=" ")
        else:
            print("{}".format(uppercase))
