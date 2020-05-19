#!/usr/bin/python3
"""This module creates a new class Square"""


class Square:
    """ Class Square constuctor method"""
    def __init__(self, size=0):
        """Initializes the data."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """The area of square"""

        """ Returns: The area of the square"""
        return(self.__size * self.__size)

    @property
    def size(self):
        """getter function"""
        """ Returns:size of square"""
        return self.__size

    @size.setter
    def size(self, val):
        """setter of attribute size"""
        if type(val) is not int:
            raise TypeError("size must be an integer")
        if val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val
