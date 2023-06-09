#!/usr/bin/python3

"""Write a class Square that defines a square by: (based on 5-square.py)"""


class Square:
    """define and initilized square"""
    def __init__(self, size=0, position=(0, 0)):
        """Assign key"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """retrieve prpoperty"""
        return self.__position

    @position.setter
    def position(self, value):
        """initilizing"""
        if (type(value) is tuple and len(value) == 2
                and type(value[0]) is int and type(value[1])
                is int and value[0] >= 0 and value[1] >= 0):
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """define the area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the character #:"""
        if self.__size == 0:
            print("")
        else:
            for a in range(self.__position[1]):
                print("")
            for b in range(self.__size):
                for c in range(self.__position[0]):
                    print(" ", end="")
                for d in range(self.__size):
                    print("#", end="")
                print("")
