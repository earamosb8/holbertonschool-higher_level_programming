#!/usr/bin/python3
"""This is module 10-square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates a Square Subclass from Rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
