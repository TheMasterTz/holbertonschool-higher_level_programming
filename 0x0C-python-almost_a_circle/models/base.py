#!/usr/bin/python3
"""
This module contains the "Base" class
"""

import json
from os import path


class Base:
    """A base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize The base class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        if type(list_dictionaries) is not list:
            raise TypeError("argument must be a list of dictionaries")

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        ListCart = []
        if list_objs is not None:
            for obj in list_objs:
                ListCart.append(cls.to_dictionary(obj))

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(ListCart))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"

        if path.exists(filename) is False:
            return []

        with open(filename, 'r', encoding='utf-8') as f:
            objs = cls.from_json_string(f.read())
            dummy = []

            for obj in objs:
                dummy.append(cls.create(**obj))
            return dummy
