#!/usr/bin/python3


"""Write a class Square that inherits from Rectangle (9-rectangle.py):"""
"""Defines a Rectangle subclass/child Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """define and initialize the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
