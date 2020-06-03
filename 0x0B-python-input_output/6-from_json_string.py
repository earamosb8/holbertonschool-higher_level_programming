#!/usr/bin/python3
"""Module for to_json_string"""
import json
"""This is module 6-from_json_string.py."""


def from_json_string(my_str):
    """returns an object (data structure) represented by a JSON string"""
    return json.loads(my_str)
