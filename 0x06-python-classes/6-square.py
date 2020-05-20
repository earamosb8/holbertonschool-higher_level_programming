#!/usr/bin/python3
"""This module creates a new class Square"""


class Square:
    """ Class Square constuctor method"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
        """setter of size"""
        if type(val) is not int:
            raise TypeError("size must be an integer")
        if val < 0:
            raise ValueError("size must be >= 0")
        self.__size = val

    def my_print(self):
        """print the size square"""
        if self.size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for i in range(self.__size):
                    print("#", end="")
                print("")

    @property
    def position(self):
        """getter function of position"""
        """Returns:position of square"""
        return self.__position

    @position.setter
    def position(self, position):
        if type(position) != tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
