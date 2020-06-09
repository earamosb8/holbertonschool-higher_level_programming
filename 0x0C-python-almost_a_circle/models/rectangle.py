#!/usr/bin/python3

"""Module for to models"""

from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor Class"""
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
        """Return a string"""
        id = str(self.id)
        width = str(self.__width)
        height = str(self.__height)
        x = str(self.__x)
        y = str(self.__y)
        string = "[Rectangle] (" + id + ") " + x + "/" + y + " - "\
            + width + "/" + height
        return string

    @property
    def width(self):
        """Getter of width"""
        return (self.__width)

    @width.setter
    def width(self, width):
        """Setter of width"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Getter of height"""
        return (self.__height)

    @height.setter
    def height(self, height):
        """Setter of height"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Getter of x"""
        return (self.__x)

    @x.setter
    def x(self, x):
        """Setter of x"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Getter of y"""
        return (self.__y)

    @y.setter
    def y(self, y):
        """Setter of y"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculate area"""
        return (self.__width * self.__height)

    def display(self):
        """
        Print the square checking position
        """
        for ejey in range(0, self.__y):
            print("")
        for q in range(0, self.__height):
            for ejex in range(0, self.__x):
                print(" ", end="")
            for p in range(0, self.__width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """update attributes"""
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
                if (hasattr(self, key)):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary"""
        new_dictionary = {}
        for key, value in self.__dict__.items():
            new_dictionary[key.split("__")[-1]] = value
        return new_dictionary
