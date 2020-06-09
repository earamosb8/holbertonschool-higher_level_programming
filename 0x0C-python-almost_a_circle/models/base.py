#!/usr/bin/python3

"""Module for Base Class"""
import json
import os


class Base:
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor of the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converto to json string"""
        if list_dictionaries is None or list_dictionaries is {}:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """from_json_string Class
        writes an Object to a text file, using a JSON representation"""
        filename = cls.__name__
        if list_objs is None:
            res = []
        else:
            list_dict = []
            for i in list_objs:
                list_dict.append(i.to_dictionary())
            res = list_dict
        with open(filename + ".json", 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(res))

    @staticmethod
    def from_json_string(json_string):
        """convert from json string"""
        if json_string is None or json_string == []:
            my_list = []
        else:
            my_list = json.loads(json_string)
        return (my_list)

    @classmethod
    def create(cls, **dictionary):
        """create a copy of instance"""
        if (cls.__name__ == "Square"):
            dummy = cls(3)
        elif (cls.__name__ == "Rectangle"):
            dummy = cls(3, 3)
        dummy.update(**dictionary)
        return(dummy)

    @classmethod
    def load_from_file(cls):
        """load json file"""
        instance_list = []
        filename = cls.__name__ + ".json"
        if not os.path.isfile(filename):
            return (instance_list)
        with open(filename) as my_file:
            my_data = cls.from_json_string(my_file.read())
            for instance in my_data:
                instance_list.append(cls.create(**instance))
        return (instance_list)
