#!/usr/bin/python3

"""Write a class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """define and initilized square"""
    def __init__(self, size=0):
        """Assign key"""
        """literate conditional statement"""
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """define the area of square"""
        return (self.__size ** 2)
