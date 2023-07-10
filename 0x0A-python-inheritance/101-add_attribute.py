#!/usr/bin/python3


"""Write a function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, name, value):
    """define add attribute calls"""
    if "__dict__" in dir(obj):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
