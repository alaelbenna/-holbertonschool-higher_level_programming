#!/usr/bin/python3
"""task 4"""


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

    def area(self):
        """returns the rectangles area"""
        return self.__height * self.__width

    def perimeter(self):
        """returns the rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints the rectangle with the character #"""
        p_rec = ""
        if self.__width == 0 or self.__height == 0:
            return p_rec
        else:
            for i in range(self.__height):
                for j in range(self.width):
                    p_rec += "#"
                if i != self.__height - 1:
                    p_rec += "\n"
            return p_rec

    def __repr__(self):
        """return a string representation of the rectangle"""
        return 'Rectangle(' + str(self.__width) + ', ' \
            + str(self.__height) + ')'
