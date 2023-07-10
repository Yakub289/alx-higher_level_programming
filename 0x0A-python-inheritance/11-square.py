#!/usr/bin/python3


"""Write a class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py)."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """define and initialize a new square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """define and returns the area of the square"""
        return (self.__size ** 2)

    def __str__(self):
        """define string representation of an instance of class square"""
        return ("[{}] {}/{}".format(type(self).__name__, self.__size,
                                    self.__size))
