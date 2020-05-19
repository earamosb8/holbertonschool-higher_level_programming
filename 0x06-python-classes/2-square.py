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
