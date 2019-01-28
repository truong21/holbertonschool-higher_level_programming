#!/usr/bin/python3
"""Unittest for class Rectangle
"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
import sys
from io import StringIO


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
        self.assertTrue(issubclass(Rectangle, Base))

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
        with self.assertRaises(TypeError):
            Rectangle()
            Rectangle(1)

    def test_ValueError(self):
        """ Tests for value error """
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 1, -1, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 1, 4, -5)
    
    def test_Area(self):
        """ Test for area """
        r1 = Rectangle(3,2)
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 56)

    def test_display(self):
        """ tests display method """
        r1 = Rectangle(2,2)
        r1_d = "##\n" \
               "##\n"
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            r1.display()
            output = out.getvalue()
            self.assertEqual(output, r1_d)
        finally:
            sys.stdout = saved_stdout

    def test_display_position(self):
        """ tests display method with x/y position"""
        r1 = Rectangle(2, 2, 2, 2)
        r1_d = "\n" \
               "\n" \
               "  ##\n" \
               "  ##\n"
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            r1.display()
            output = out.getvalue()
            self.assertEqual(output, r1_d)
        finally:
            sys.stdout = saved_stdout
    
    def test_str_method(self):
        """ Test if __str__ method prints correct line """
        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/0 - 5/5")

    def test_update(self):
        """ test update function """
        Base._Base__nb_objects = 0
        r1 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 1/1 - 1/1")
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 1/1 - 1/1")
        r1.update(89, 2, 3, 5, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 5/5 - 2/3")
        r1.update(y=1, width=2, x=3, id=87)
        self.assertEqual(r1.__str__(), "[Rectangle] (87) 3/1 - 2/3")
        r1.update(**{'fake': 666, 'test': 'fake'})
        self.assertEqual(r1.__str__(), "[Rectangle] (87) 3/1 - 2/3")
        r1.update(**{'x': 5, 'height': 6, 'y': 7, 'width': 8})
        self.assertEqual(r1.__str__(), "[Rectangle] (87) 5/7 - 8/6")

    def test_dict(self):
        """ tests if to_dictionary method returns correct dictionary """
        Base._Base__nb_objects = 0
        r1 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 1/1 - 1/1")
        self.assertEqual(r1.to_dictionary(), {'id': 1, 'width': 1,
            'height': 1, 'x': 1, 'y': 1})
        self.assertIs(type(r1.to_dictionary()), dict)
        r2 = Rectangle(2, 2)
        self.assertEqual(r2.__str__(), "[Rectangle] (2) 0/0 - 2/2")
        self.assertEqual(r2.to_dictionary(), {'id': 2, 'width': 2,
            'height': 2, 'x': 0, 'y': 0})

if __name__ == '__main__':
    unittest.main()
