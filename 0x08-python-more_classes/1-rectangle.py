#!/usr/bin/python3
"""task 1"""


class Rectangle:
    """
    A class that defines a rectangle
    Args:
        width(int): width of the rectangle
        height(int): height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """initialisation"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns the width"""
        return self.__width

    @property
    def height(self):
        """returns the height"""
        return self.__height

    @width.setter
    def width(self, value):
        """setting width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """setting height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
