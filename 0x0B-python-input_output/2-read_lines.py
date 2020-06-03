#!/usr/bin/python3
"""This is module 2-read_lines"""


def read_lines(filename="", nb_lines=0):
    """read a number of the lines of a file"""
    with open('my_file_0.txt', 'r', encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for x in range(0, nb_lines):
                print(f.readline(), end="")
