#!/usr/bin/python3
"""Module for to models"""
from models.rectangle import Rectangle
"""This is module Rectangle."""


class Square(Rectangle):
    """This is module class base"""

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        """ width setter """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        return ("[Square] ({:d}) {:d}/{:d} - {:d}\
    ".format(self.id, self.x, self.y, self.width))
