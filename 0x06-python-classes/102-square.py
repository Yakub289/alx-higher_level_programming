#!/usr/bin/python3

"""Write a class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """define and initilized square"""
    def __init__(self, size=0):
        """Assign key"""
        self.__size = size

    @property
    def size(self):
        """retrieve prpoperty"""
        return self.__size

    @size.setter
    def size(self, value):
        """initilizing the value size"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """define the area of square"""
        return (self.__size ** 2)

    def __eq__(self, comparactor):
        """comparactor == assign (equal sign)"""
        return self.__size == comparactor.__size

    def __ne__(self, comparactor):
        """comparactor != assign (not equal sign)"""
        return self.__size != comparactor.__size

    def __gt__(self, comparactor):
        """comparactor > assign (greater than)"""
        return self.__size > comparactor.__size

    def __ge__(self, comparactor):
        """comparactor >= assign (greater than or equal)"""
        return self.__size >= comparactor.__size

    def __lt__(self, comparactor):
        """comparactor < assign (less than)"""
        return self.__size < comparactor.__size

    def __le__(self, comparactor):
        """comparactor <= assign (less than or equal)"""
        return self.__size <= comparactor.__size
