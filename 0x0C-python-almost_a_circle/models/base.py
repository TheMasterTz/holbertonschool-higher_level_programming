"""
This module contains the "Base" class
"""

import json

class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        ListCart = []
        if list_objs is not None:
            for obj in list_objs:
                ListCart.append(cls.to_json_string(obj))

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(ListCart))

