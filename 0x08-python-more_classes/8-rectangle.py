#!/usr/bin/python3

"""Write a class Rectangle that defines a rectangle(based on 6-rectangle.py)"""


class Rectangle:
    """initilize instance of a number"""
    number_of_instances = 0
    """change attribute with new representation"""
    print_symbol = "#"
    """define and initilizing rectangle"""
    def __init__(self, width=0, height=0):
        """assign keys"""
        self.width = width
        self.height = height
        """increment the number instance after each new instantiation"""
        type(self).number_of_instances = (self).number_of_instances + 1

    @property
    def width(self):
        """define width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """assign width value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """define height"""
        return (self.__height)

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

    def __str__(self):
        """define string representation of the rectangle & return comparison"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        for column in range(self.__height):
            for row in range(self.__width):
                print(self.print_symbol, end="")
            if column < (self.__height - 1):
                print("")
        return ("")

    def __repr__(self):
        """format the string representation of the rectangle"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """define the delete action on the rectangle"""
        print("Bye rectangle...")
        """decrement the number instance after deletion"""
        type(self).number_of_instances = (self).number_of_instances - 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """define and returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
