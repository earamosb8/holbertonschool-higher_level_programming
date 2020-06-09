#!/usr/bin/python3

"""Module for to models"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor Class"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter of size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """ width setter """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """String magic Returns:
           string"""
        id = str(self.id)
        x = str(self.x)
        y = str(self.y)
        size = str(self.width)
        string = "[Square] (" + id + ") " + x + "/" + y + " - " + size
        return string

    def update(self, *args, **kwargs):
        """update attributes"""
        l = len(args)
        if args and l > 0:
            for arg in args:
                if type(arg) is not int:
                    raise ValueError("arg must be integer")
            if l >= 1:
                self.id = args[0]
            if l >= 2:
                self.size = args[1]
            if l >= 3:
                self.x = args[2]
            if l >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if (hasattr(self, key)):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary"""
        new_dictionary = {}
        for key, value in self.__dict__.items():
            k = key.split("__")[-1]
            if k == "width" or k == "height":
                new_dictionary["size"] = value
            else:
                new_dictionary[key.split("__")[-1]] = value
        return new_dictionary
