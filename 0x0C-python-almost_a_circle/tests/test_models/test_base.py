#!/usr/bin/python3

"""
Unittest for base([..])
"""

import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """ class TestBase"""

    def test_base(self):
        """tests for base"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        self.assertIsInstance(b1, Base)

        b2 = Base()
        self.assertEqual(b2.id, 2)
        self.assertIsInstance(b2, Base)

        b3 = Base(9)
        self.assertEqual(b3.id, 9)
        self.assertIsInstance(b3, Base)

        b4 = Base()
        self.assertEqual(b4.id, 3)
        self.assertIsInstance(b4, Base)

        b5 = Rectangle(12, 3, 5 ,7)
        Dict = b5.to_dictionary()
        Dict2 = {'x': 5, 'width': 12, 'id': 4, 'height': 3, 'y': 7}
        self.assertDictEqual(Dict, Dict2)
        self.assertIsInstance(Base.to_json_string([Dict]), str)
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")

        Rectangle.save_to_file([])
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(f.read(), "[]")

        Rectangle.save_to_file(None)
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(f.read(), "[]")

        Square.save_to_file([])
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(f.read(), "[]")

        Square.save_to_file(None)
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(f.read(), "[]")


if __name__ == "__main__":
    unittest.main()
