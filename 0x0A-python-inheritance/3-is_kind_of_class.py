#!/usr/bin/python3


"""Write a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False."""


def is_kind_of_class(obj, a_class):
    """define is kind of a class and return the value of the class"""
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)