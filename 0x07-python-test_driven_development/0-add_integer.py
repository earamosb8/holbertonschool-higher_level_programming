#!/usr/bin/python3
"""This is the 0-add_integer module."""


def add_integer(a, b=98):
    """Does the addition of two integers"""
    """Arguments a and b can be integer or float"""
    """Return:a + b or raise error if input not a number"""
    if isinstance(a, str) or a is None:
        raise TypeError("a must be an integer")
    if isinstance(b, str) or b is None:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
