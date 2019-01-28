#!/usr/bin/python3
"""Unittest for class Square
"""

import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import sys
from io import StringIO


class TestSquareClass(unittest.TestCase):
    """Testing module for class Square"""
    def test_id(self):
        """ Test square id tracking """
        Base._Base__nb_objects = 0
        s1 = Square(10)
        s2 = Square(2, 1)
        s3 = Square(10, 0, 0, 12)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 12)
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(issubclass(Square, Rectangle))

    def test_TypeError(self):
        """ Tests for type error """
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r4 = Square("dog", 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r6 = Square(10, "cat", 0)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r7 = Square(10, 4, "test")
        with self.assertRaises(TypeError):
            Square()
            Square(1)

    def test_ValueError(self):
        """ Tests for value error """
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -1, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 1, -5)


if __name__ == '__main__':
    unittest.main()
