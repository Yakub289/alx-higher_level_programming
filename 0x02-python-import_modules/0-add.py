#!/usr/bin/python3

# Write a program that imports the function def add(a, b):
# from the file add_0.py and prints the result of the addition 1 + 2 = 3.

def add(a,b):
    a = 1
    b = 2
    result = a + b
    print("<a value> + <b value> = <add(a, b) value>: ", "{:d}".format(result))
    add("a,b", "result")
