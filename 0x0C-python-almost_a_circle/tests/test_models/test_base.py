#!/usr/bin/python3
"""Unittest for class Base
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """Testing module for class Base"""
    def test_id(self):
        """Test base id increment"""
        b1 = Base()
        b2 = Base()
        b5 = Base(5)
        b4 = Base("dog")
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b5.id, 5)
        self.assertEqual(b4.id, "dog")
        self.assertEqual(b3.id, 3)

    def test_to_json_string(self):
        """ test to see return of JSON string """
        Base._Base__nb_objects = 0
        rect = Rectangle(10, 7, 2, 8, 1)
        dictionary = rect.to_dictionary()
        j = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(dictionary, j)
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_dictionary), str)

    def test_from_json_string(self):
        """ test for from_json_string """
        Base._Base__nb_objects = 0
        """ empty string or None arguments """
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        """ test a list of input """
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_input), list)
        self.assertEqual(type(json_list_input), str)
        self.assertEqual(type(list_output), list)

    def test_create(self):
        """ test for rectangle or square creation """
        Base._Base__nb_objects = 0
        s1 = Square(11, 22, 33, 44)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertFalse(s1 is s2)
        self.assertFalse(s1 == s2)

        r1 = Square(3, 6, 1)
        r1_dict = r1.to_dictionary()
        r2 = Square.create(**r1_dict)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_load_from_file(self):
        """ testing load_from_file method """
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()
        self.assertNotEqual(list_rectangles_input, list_rectangles_output)

if __name__ == '__main__':
    unittest.main()
