#!/usr/bin/python3
"""
This module contains the "Base" class
"""

import json
import csv
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
        List = []

        if list_objs is not None:
            for obj in list_objs:
                List.append(cls.to_dictionary(obj))

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(List))

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """def save_to_file_csv"""
        filename = cls.__name__ + ".csv"

        with open(filename, 'w') as filecsv:
            write = csv.writer(filecsv)
            if cls.__name__ is "Rectangle":
                for obj in list_objs:
                    write.writerow([obj.id, obj.width, obj.height,
                                    obj.x, obj.y])
            if cls.__name__ is "Square":
                for obj in list_objs:
                    write.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """def save_to_csv"""
        filename = cls.__name__ + ".csv"
        List = []

        try:
            with open(filename, 'r') as fcsv:
                reader = csv.reader(fcsv)
                for args in reader:
                    if cls.__name__ is "Rectangle":
                        dictionary = {
                            "id": int(args[0]),
                            "width": int(args[1]),
                            "height": int(args[2]),
                            "x": int(args[3]),
                            "y": int(args[4])
                        }
                    if cls.__name__ is "Square":
                        dictionary = {
                            "id": int(args[0]),
                            "size": int(args[1]),
                            "x": int(args[2]),
                            "y": int(args[3])
                        }
                    List.append(cls.create(**dictionary))
        except:
            pass
        return List
