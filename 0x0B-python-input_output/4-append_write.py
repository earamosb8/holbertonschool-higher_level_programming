#!/usr/bin/python3
"""This is module 4-append_write"""


def append_write(filename="", text=""):
    """append a string to a file"""
    with open(filename, mode="a", encoding="utf-8") as f:
        count = f.write(text)
    return count
