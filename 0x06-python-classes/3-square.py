#!/usr/bin/python3
"""
Class Square: contains optional size, area
"""


class Square:
    """Create an square with private instance attribute: size"""
    def __init__(self, size=0):
        """ instantiation with optional size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """ instantiation with area """
    def area(self):
        return self.__size ** 2
