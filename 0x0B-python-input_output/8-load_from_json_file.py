#!/usr/bin/python3
import json
"""This is module 8-load_from_json."""


def load_from_json_file(filename):
    """Creates a python object from a text file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
