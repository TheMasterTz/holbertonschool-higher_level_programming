# !/usr/bin/python3

"""
Unittest for base([..])
"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test Rectangle"""

    def test_rectangle(self):
        """Test rectangles"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertIsInstance(r1, Rectangle)
        self.assertIsInstance(r1, Base)

        r2 = Rectangle(2, 10, 5)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 5)
        self.assertEqual(r2.y, 0)
        self.assertIsInstance(r2, Rectangle)
        self.assertIsInstance(r2, Base)

        r3 = Rectangle(3, 12, 3, 6)
        self.assertEqual(r3.width, 3)
        self.assertEqual(r3.height, 12)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 6)
        self.assertIsInstance(r3, Rectangle)
        self.assertIsInstance(r3, Base)

        r4 = Rectangle(10, 2)
        self.assertEqual(r4.area(), 20)

        r5 = Rectangle(2, 3, 1)
        self.assertEqual(r5.area(), 6)

        # width, height, x = 0, y = 0, id = None)
        r6 = Rectangle(4, 5, 10, 7, 3)
        self.assertEqual(r6.__str__(), "[Rectangle] (3) 10/7 - 4/5")
        r6.update(89)
        self.assertEqual(r6.__str__(), "[Rectangle] (89) 10/7 - 4/5")
        r6.update(89, 2)
        self.assertEqual(r6.__str__(), "[Rectangle] (89) 10/7 - 2/5")
        r6.update(89, 2, 10)
        self.assertEqual(r6.__str__(), "[Rectangle] (89) 10/7 - 2/10")
        r6.update(89, 2, 10, 4)
        self.assertEqual(r6.__str__(), "[Rectangle] (89) 4/7 - 2/10")
        r6.update(89, 2, 10, 4, 1)
        self.assertEqual(r6.__str__(), "[Rectangle] (89) 4/1 - 2/10")

        r7 = Rectangle(3, 5, 1, 3, 10)
        self.assertEqual(r7.__str__(), "[Rectangle] (10) 1/3 - 3/5")
        r7.update(id=89)
        self.assertEqual(r7.__str__(), "[Rectangle] (89) 1/3 - 3/5")
        r7.update(x=4, y=10)
        self.assertEqual(r7.__str__(), "[Rectangle] (89) 4/10 - 3/5")
        r7.update(width=4, height=1)
        self.assertEqual(r7.__str__(), "[Rectangle] (89) 4/10 - 4/1")

        r8 = Rectangle(3, 5, 1, 3, 10)
        self.assertEqual(r8.__str__(), "[Rectangle] (10) 1/3 - 3/5")

        r9 = Rectangle(4, 5, 10, 7, 3)
        self.assertEqual(r9.__str__(), "[Rectangle] (3) 10/7 - 4/5")

        r10 = Rectangle(10, 12, 3, 4, 14)
        Newdict = {'width': 10, 'height': 12, 'id': 14, 'x': 3, 'y': 4}
        self.assertEqual(r10.to_dictionary(), Newdict)
        self.assertEqual(r10.__str__(), "[Rectangle] (14) 3/4 - 10/12")
        self.assertIsInstance(r10.to_dictionary(), dict)
        self.assertIsInstance(r10, Rectangle)

        r11 = Rectangle(1, 1)
        r11.update(**r10.to_dictionary())
        self.assertEqual(r11.__str__(), "[Rectangle] (14) 3/4 - 10/12")
        self.assertFalse(r11 == r10)

        # TypeError width
        with self.assertRaises(TypeError) as error:
            Rectangle("hi", 11)
        self.assertEqual("width must be an integer", str(error.exception))
        with self.assertRaises(TypeError) as error:
            Rectangle([], 11)
        self.assertEqual("width must be an integer", str(error.exception))
        with self.assertRaises(TypeError) as error:
            Rectangle((10, ), 11)
        self.assertEqual("width must be an integer", str(error.exception))
        with self.assertRaises(TypeError) as error:
            Rectangle({}, 11)
        self.assertEqual("width must be an integer", str(error.exception))
        with self.assertRaises(TypeError) as error:
            Rectangle(7.34, 11)
        self.assertEqual("width must be an integer", str(error.exception))
        with self.assertRaises(TypeError) as error:
            Rectangle(True, 11)
        self.assertEqual("width must be an integer", str(error.exception))
        with self.assertRaises(ValueError) as error:
            Rectangle(-4, 11)
        self.assertEqual("width must be > 0", str(error.exception))

        # TypeError height
        with self.assertRaises(TypeError) as error:
            Rectangle(11, "11")
        self.assertEqual("height must be an integer", str(error.exception))
        with self.assertRaises(TypeError) as error:
            Rectangle(11, [])
        self.assertEqual("height must be an integer", str(error.exception))
        with self.assertRaises(TypeError) as error:
            Rectangle(11, {})
        self.assertEqual("height must be an integer", str(error.exception))
        with self.assertRaises(TypeError) as error:
            Rectangle(11, (1, 2))
        self.assertEqual("height must be an integer", str(error.exception))
        with self.assertRaises(TypeError) as error:
            Rectangle(11, True)
        self.assertEqual("height must be an integer", str(error.exception))
        with self.assertRaises(TypeError) as error:
            Rectangle(11, 2.23)
        self.assertEqual("height must be an integer", str(error.exception))
        with self.assertRaises(ValueError) as error:
            Rectangle(11, -3)
        self.assertEqual("height must be > 0", str(error.exception))

        # TypeError x
        with self.assertRaises(TypeError) as error:
            Rectangle(11, 12, "hi")
        self.assertEqual("x must be an integer", str(error.exception))
        with self.assertRaises(TypeError) as error:
            Rectangle(11, 12, {})
        self.assertEqual("x must be an integer", str(error.exception))
        with self.assertRaises(TypeError) as error:
            Rectangle(11, 12, [])
        self.assertEqual("x must be an integer", str(error.exception))
        with self.assertRaises(TypeError) as error:
            Rectangle(11, 12, (1, 2))
        self.assertEqual("x must be an integer", str(error.exception))
        with self.assertRaises(TypeError) as error:
            Rectangle(11, 12, False)
        self.assertEqual("x must be an integer", str(error.exception))
        with self.assertRaises(TypeError) as error:
            Rectangle(11, 12, 4.22)
        self.assertEqual("x must be an integer", str(error.exception))
        with self.assertRaises(ValueError) as error:
            Rectangle(11, 12, -2)
        self.assertEqual("x must be >= 0", str(error.exception))

        # TypeError y
        with self.assertRaises(TypeError) as error:
            Rectangle(11, 12, 3, "hi")
        self.assertEqual("y must be an integer", str(error.exception))
        with self.assertRaises(TypeError) as error:
            Rectangle(11, 12, 3, [])
        self.assertEqual("y must be an integer", str(error.exception))
        with self.assertRaises(TypeError) as error:
            Rectangle(11, 12, 3, {})
        self.assertEqual("y must be an integer", str(error.exception))
        with self.assertRaises(TypeError) as error:
            Rectangle(11, 12, 3, (2, 5))
        self.assertEqual("y must be an integer", str(error.exception))
        with self.assertRaises(TypeError) as error:
            Rectangle(11, 12, 3, False)
        self.assertEqual("y must be an integer", str(error.exception))
        with self.assertRaises(TypeError) as error:
            Rectangle(11, 12, 3, 5.67)
        self.assertEqual("y must be an integer", str(error.exception))
        with self.assertRaises(ValueError) as error:
            Rectangle(11, 12, 3, -2)
        self.assertEqual("y must be >= 0", str(error.exception))


if __name__ == '__main__':
    unittest.main()
