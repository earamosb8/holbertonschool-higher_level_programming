#!/usr/bin/python3
"""This is module 1-number_of_lines"""


def number_of_lines(filename=""):
    """print the lines of a file"""

    lines = 0
    with open('my_file_0.txt', 'r', encoding="utf-8") as f:
        for line in f:
            lines += 1
    return lines
