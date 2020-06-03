#!/usr/bin/python3
"""This is module 0-read_file"""


def read_file(filename=""):
    """reads and prints a file"""

    with open('my_file_0.txt', 'r', encoding="utf-8") as f:
        read_data = f.read()
    print(read_data, end="")
