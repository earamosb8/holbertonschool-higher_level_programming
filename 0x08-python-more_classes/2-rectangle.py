#!/usr/bin/python3
""" This module creates a new class Rectangle"""


class Rectangle():
    """Class Rectangle constructor method """

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Getter of Rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of Rectangle width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter of Rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of Rectangle height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Return the perimeter of Rectangle"""
        return ((2 * self.__height) + (2 * self.__width))
