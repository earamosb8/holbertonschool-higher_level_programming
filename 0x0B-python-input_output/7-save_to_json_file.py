#!/usr/bin/python3
"""Module for to_json_string"""
import json
"""This is module 7-save_to_json_file"""


def save_to_json_file(my_obj, filename):
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
