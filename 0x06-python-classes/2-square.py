#!/usr/bin/python3

"""Write a class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """define and initilized square"""
    def __init__(self, size=0):
        """Assign key"""
        self.__size = size
        """ileterate conditionl statement"""
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                raise TypeError("size must be an integer")
