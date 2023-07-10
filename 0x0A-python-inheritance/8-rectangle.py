#!/usr/bin/python3


"""Write a class Rectangle that inherit of BaseGeometry(7-base_geometry.py)"""
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a class to define rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """define the init and each parameter"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
