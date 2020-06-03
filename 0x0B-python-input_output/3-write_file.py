#!/usr/bin/python3
"""This is module 3-write_file"""


def write_file(filename="", text=""):
    """write a string to a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        charsw = f.write(text)
    return(charsw)
