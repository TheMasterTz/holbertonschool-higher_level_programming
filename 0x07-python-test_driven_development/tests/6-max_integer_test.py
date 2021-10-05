#!/usr/bin/python3
"""
Unittest for max_integer([..])

"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A class to test a max integer function
    """

    def test_max_integer(self):
        """
        Test the max integer in a list of integers when the integers
        are positive or negative numbers
        """
        self.assertEqual(max_integer([4, 3, 2, 10]), 10)
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([34, 3.543, 22.431234]), 34)
        self.assertEqual(max_integer([-40, -3, -2, 0]), 0)
        self.assertEqual(max_integer([9.788]), 9.788)

    def test_wrong_type(self):
        """
        Test the max integer with wrong parameters types
        """
        with self.assertRaises(TypeError):
            max_integer(None)

        with self.assertRaises(TypeError):
            max_integer(["jose", 23, 4, 1, -9])


if __name__ == '__main__':
    unittest.main()
