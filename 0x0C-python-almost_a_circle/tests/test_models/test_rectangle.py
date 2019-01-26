#!/usr/bin/python3
"""Unittest for class Rectangle
"""

import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    """Testing module for class Rectangle"""
    def test_id(self):
        """ Test base rectangle """
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_TypeError(self):
        """ Tests for type error """
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r4 = Rectangle("dog", 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r6 = Rectangle(4, "Test")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r6 = Rectangle(10, 2, "cat", 0)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r7 = Rectangle(10, 2, 4, "test")

    def test_ValueError(self):
        """ Tests for value error """
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(ValueError, "width must be an integer"):
            Rectangle(-1, 0)
        with self.assertRaisesRegex(ValueError, "height must be an integer"):
            Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "x must be an integer"):
            Rectangle(1, 1, -1, 0)
        with self.assertRaisesRegex(ValueError, "y must be an integer"):
            Rectangle(1, 1, 4, -5)

if __name__ == '__main__':
    unittest.main()
