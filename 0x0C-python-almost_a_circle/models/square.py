"""
This module contains the "Square" class
"""

from .rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        if len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "y" in kwargs:
                self.y = kwargs["y"]
            if "id" in kwargs:
                self.id = kwargs["id"]
    def to_dictionary(self):
        dictionary = {}

        dictionary["id"] = self.id
        dictionary["x"] = self.x
        dictionary["size"] = self.size
        dictionary["y"] = self.y

        return dictionary
