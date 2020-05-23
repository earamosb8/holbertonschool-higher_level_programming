#!/usr/bin/python3
"""This is the 4-print_square."""


def print_square(size):
    """this functions print a square with size"""

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise ValueError("size must be an integer")
    for i in range(0, size):
        for x in range(0, size):
            print('#', end="")
        print("")
