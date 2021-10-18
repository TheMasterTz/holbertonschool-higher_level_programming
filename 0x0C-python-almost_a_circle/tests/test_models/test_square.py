# !/usr/bin/python3

"""
Unittest for base([..])
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """class TestSquare"""
    def test_square(self):
        """tests for Square class"""
        s1 = Square(5, 0, 0, 1)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.area(), 25)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        self.assertIsInstance(s1, Rectangle)
        self.assertIsInstance(s1, Base)
        self.assertIsInstance(s1, Square)

        s2 = Square(5, 8, 0, 45)
        self.assertEqual(s2.size, 5)
        self.assertEqual(s2.width, 5)
        self.assertEqual(s2.height, 5)
        self.assertEqual(s2.x, 8)
        self.assertEqual(s2.y, 0)
        self.assertEqual(s2.area(), 25)
        self.assertEqual(s2.__str__(), "[Square] (45) 8/0 - 5")
        self.assertIsInstance(s2, Rectangle)
        self.assertIsInstance(s2, Base)
        self.assertIsInstance(s2, Square)

        s3 = Square(4, 2, 6, 89)
        self.assertEqual(s3.size, 4)
        self.assertEqual(s3.width, 4)
        self.assertEqual(s3.height, 4)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 6)
        self.assertEqual(s3.area(), 16)
        self.assertEqual(s3.__str__(), "[Square] (89) 2/6 - 4")
        self.assertIsInstance(s3, Rectangle)
        self.assertIsInstance(s3, Base)
        self.assertIsInstance(s3, Square)

        s4 = Square(4, 2, 6, 89)
        self.assertEqual(s4.__str__(), "[Square] (89) 2/6 - 4")
        s4.update(10)
        self.assertEqual(s4.__str__(), "[Square] (10) 2/6 - 4")
        s4.update(10, 2)
        self.assertEqual(s4.__str__(), "[Square] (10) 2/6 - 2")
        s4.update(10, 2, 3)
        self.assertEqual(s4.__str__(), "[Square] (10) 3/6 - 2")
        s4.update(10, 2, 3, 4)
        self.assertEqual(s4.__str__(), "[Square] (10) 3/4 - 2")

        s5 = Square(4, 2, 6, 89)
        self.assertEqual(s5.__str__(), "[Square] (89) 2/6 - 4")
        s5.update(id = 10)
        self.assertEqual(s5.__str__(), "[Square] (10) 2/6 - 4")
        s5.update(x = 3, y = 6)
        self.assertEqual(s5.__str__(), "[Square] (10) 3/6 - 4")
        s5.update(size = 2)
        self.assertEqual(s5.__str__(), "[Square] (10) 3/6 - 2")

        s6 = Square(5, 4, 2, 10)
        Newdict = {'id': 10, 'x': 4, 'size': 5, 'y': 2}
        self.assertEqual(s6.to_dictionary(), Newdict)
        self.assertEqual(s6.__str__(), "[Square] (10) 4/2 - 5")
        self.assertIsInstance(s6.to_dictionary(), dict)
        self.assertIsInstance(s6, Rectangle)
        self.assertIsInstance(s6, Square)

        s7 = Square(1, 1)
        s7.update(**s6.to_dictionary())
        self.assertEqual(s7.__str__(), "[Square] (10) 4/2 - 5")
        self.assertEqual(s7 == s6, False)


        #TypeError size
        with self.assertRaises(TypeError) as error:
            Square("hi")
        self.assertEqual("width must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            Square({})
        self.assertEqual("width must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            Square([])
        self.assertEqual("width must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            Square((1, 2))
        self.assertEqual("width must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            Square(2.34)
        self.assertEqual("width must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            Square(True)
        self.assertEqual("width must be an integer", str(error.exception))

        with self.assertRaises(ValueError) as error:
            Square(-4)
        self.assertEqual("width must be >= 0", str(error.exception))


        #TypeError x
        with self.assertRaises(TypeError) as error:
            Square(11 , "hi")
        self.assertEqual("x must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            Square(11 , {})
        self.assertEqual("x must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            Square(11 , [])
        self.assertEqual("x must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            Square(11 , (1, 2))
        self.assertEqual("x must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            Square(11 , 3.45)
        self.assertEqual("x must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            Square(11 , False)
        self.assertEqual("x must be an integer", str(error.exception))

        with self.assertRaises(ValueError) as error:
            Square(11 , -5)
        self.assertEqual("x must be >= 0", str(error.exception))


        #TypeError y
        with self.assertRaises(TypeError) as error:
            Square(11 , 3, "hi")
        self.assertEqual("y must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            Square(11 , 3, {})
        self.assertEqual("y must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            Square(11 , 3, [])
        self.assertEqual("y must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            Square(11 , 3, (1, 2))
        self.assertEqual("y must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            Square(11 , 3, 3.45)
        self.assertEqual("y must be an integer", str(error.exception))

        with self.assertRaises(TypeError) as error:
            Square(11 , 3, False)
        self.assertEqual("y must be an integer", str(error.exception))

        with self.assertRaises(ValueError) as error:
            Square(11 , 3, -5)
        self.assertEqual("y must be >= 0", str(error.exception))

if __name__ == "__main__":
    unittest.main()
