#!/usr/bin/python3
class MyList(list):
    """class representing a list"""

    def print_sorted(self):
        """print the list sorted"""
        print(sorted(self))
