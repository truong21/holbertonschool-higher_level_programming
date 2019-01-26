#!/usr/bin/python3
"""Unittest for class Base
"""

import unittest
from models.base import Base


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

if __name__ == '__main__':
    unittest.main()
