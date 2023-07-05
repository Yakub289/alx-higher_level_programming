#!/usr/bin/python3

"""Write a function that adds 2 integers."""


def add_integer(a, b=98):
    """define two variable, add return and check their datatype"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return (int(a) +int(b))
