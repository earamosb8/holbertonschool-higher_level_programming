#!/usr/bin/python3
""" This module creates a new class Rectangle"""


class Rectangle:
    """Class Rectangle constructor method """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the class Rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.__height == 0 or self.__width == 0:
            return (0)
        else:
            return ((2 * self.__height) + (2 * self.__width))

    def __str__(self):
        """String representation of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            return("\n".join(["{}".format(self.print_symbol) *
                              self.__width for i in range(self.__height)]))

    def __repr__(self):
        """String representation of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            rps = '{self.__class__.__name__}({self.width}, {self.height})\
'.format(self=self)
            return(rps)

    def __del__(self):
        """Delete instance of object"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares 2 rectangles"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return(rect_2)

    @classmethod
    def square(cls, size=0):
        """Creates a square"""
        return (cls(size, size))
