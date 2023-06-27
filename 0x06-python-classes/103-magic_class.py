#!/usr/bin/python3

import math
"""Write the Python class MagicClass"""


class MagicClass:
    """define and initilize MagicClass."""
    def __init__(self, radius=0):
        """Initializing key and condition statement"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate the area of a circle"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Calculate the circumference of a circle"""
        return (2 * math.pi * self.__radius)
