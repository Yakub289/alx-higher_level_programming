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

    def my_print(self):
        """prints in stdout the square with the character #:"""
        if self.__size == 0:
            print()
        else:
            for ink in range(self.__size):
                for pen in range(self.__size):
                    print("#", end="")
                print("")
