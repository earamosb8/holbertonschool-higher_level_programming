#!/usr/bin/python3
import json
import os
"""This is module class base"""


class Base:
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects = Base.__nb_objects + 1

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        tmp_list = [x.to_dictionary() for x in list_objs]
        filename = cls.__name__ + ".json"
        with open(filename, "w") as my_file:
            my_file.write(cls.to_json_string(tmp_list))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == []:
            return ("[]")
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        if (cls.__name__ == "Square"):
            dummy = cls(3)
        elif (cls.__name__ == "Rectangle"):
            dummy = cls(3, 3)
        dummy.update(**dictionary)
        return(dummy)

    @classmethod
    def load_from_file(cls):
        instance_list = []
        filename = cls.__name__ + ".json"
        if not os.path.isfile(filename):
            return (instance_list)
        with open(filename) as my_file:
            my_data = cls.from_json_string(my_file.read())
            for instance in my_data:
                instance_list.append(cls.create(**instance))
        return (instance_list)
