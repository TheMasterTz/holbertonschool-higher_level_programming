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
    """class TestBase"""

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

        b5 = Rectangle(12, 3, 5, 7)
        Dict = b5.to_dictionary()
        Dict2 = {'x': 5, 'width': 12, 'id': 4, 'height': 3, 'y': 7}
        self.assertDictEqual(Dict, Dict2)
        self.assertIsInstance(Base.to_json_string([Dict]), str)
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")

        with self.assertRaises(TypeError) as error:
            Base.to_json_string(5)
        self.assertEqual("argument must be a list of dictionaries",
                         str(error.exception))
        with self.assertRaises(TypeError) as error:
            Base.to_json_string("hi")
        self.assertEqual("argument must be a list of dictionaries",
                         str(error.exception))
        with self.assertRaises(TypeError) as error:
            Base.to_json_string((1, ))
        self.assertEqual("argument must be a list of dictionaries",
                         str(error.exception))
        with self.assertRaises(TypeError) as error:
            Base.to_json_string({})
        self.assertEqual("argument must be a list of dictionaries",
                         str(error.exception))
        with self.assertRaises(TypeError) as error:
            Base.to_json_string(True)
        self.assertEqual("argument must be a list of dictionaries",
                         str(error.exception))
        with self.assertRaises(TypeError) as error:
            Base.to_json_string(-1)
        self.assertEqual("argument must be a list of dictionaries",
                         str(error.exception))

        with self.assertRaises(AttributeError) as error:
            Rectangle.save_to_file({'hi': 'hi'})
        self.assertEqual("'str' object has no attribute 'x'",
                         str(error.exception))
        with self.assertRaises(TypeError) as error:
            Rectangle.save_to_file(5)
        self.assertEqual("'int' object is not iterable",
                         str(error.exception))
        with self.assertRaises(TypeError) as error:
            Rectangle.save_to_file(False)
        self.assertEqual("'bool' object is not iterable",
                         str(error.exception))
        with self.assertRaises(AttributeError) as error:
            Rectangle.save_to_file("hi")
        self.assertEqual("'str' object has no attribute 'x'",
                         str(error.exception))
        with self.assertRaises(AttributeError) as error:
            Rectangle.save_to_file([4, 5])
        self.assertEqual("'int' object has no attribute 'x'",
                         str(error.exception))
        with self.assertRaises(AttributeError) as error:
            Rectangle.save_to_file([False, True])
        self.assertEqual("'bool' object has no attribute 'x'",
                         str(error.exception))
        with self.assertRaises(AttributeError) as error:
            Rectangle.save_to_file(["hi", "world", "list"])
        self.assertEqual("'str' object has no attribute 'x'",
                         str(error.exception))

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

        t1 = Base()
        t2 = Base()

        with self.assertRaises(AttributeError) as error:
            Rectangle.save_to_file([t1, t2])
        self.assertEqual("'Base' object has no attribute 'x'",
                         str(error.exception))

        self.assertEqual(Rectangle.from_json_string(None), [])
        self.assertEqual(Rectangle.from_json_string(""), [])


if __name__ == "__main__":
    unittest.main()
