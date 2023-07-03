#!/usr/bin/python3

"""Write a class Rectangle that defines a rectangle(based on 1-rectangle.py)"""


class Rectangle:
    """define and initilizing rectangle"""
    def __init__(self, width=0, height=0):
        """assign keys"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """define width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            """assign width value"""
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """define height"""
        return self.__height

    @height.setter
    def height(self, value):
        """assign height value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """define area of the rectangle and set the return value"""
        return (self.__width * self.__height)

    def perimeter(self):
        """define perimeter of the rectangle and set the return value"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
