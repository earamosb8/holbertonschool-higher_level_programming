#!/usr/bin/python3
"""This is module 6-base_geometry"""


class BaseGeometry:
    """empty class BaseGeometry"""
    pass

    def area(self):
        """ Not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the choice of value for name"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
