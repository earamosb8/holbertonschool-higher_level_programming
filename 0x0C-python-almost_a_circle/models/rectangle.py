#!/usr/bin/python3
"""Module for to models"""
from models.base import Base
"""This is module Rectangle."""


class Rectangle(Base):
    """This is module class base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    def __str__(self):
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}\
    ".format(self.id, self.__x, self.__y, self.__width, self.__height))

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        return (self.__width * self.__height)

    def display(self):
        for ejey in range(0, self.__y):
            print("")
        for q in range(0, self.__height):
            for ejex in range(0, self.__x):
                print(" ", end="")
            for p in range(0, self.__width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        l = len(args)
        if args and l > 0:
            for arg in args:
                if type(arg) is not int:
                    raise ValueError("arg must be integer")
            if l >= 1:
                self.id = args[0]
            if l >= 2:
                self.__width = args[1]
            if l >= 3:
                self.__height = args[2]
            if l >= 4:
                self.__x = args[3]
            if l >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
