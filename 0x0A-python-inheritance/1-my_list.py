#!/usr/bin/python3
""" this module create the class Mylist"""


class MyList(list):
    """class representing a list"""

    def print_sorted(self):
        """print the list sorted"""
        print(sorted(self))
