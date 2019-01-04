#!/usr/bin/python3
"""
Class Square: contains optional size, area
"""


class Square:
    """Create an square with private instance attribute: size"""
    def __init__(self, size=0):
        """ initializes a square with attributes """
        self.__size = size

    @property
    def size(self):
        """ retrieves the size """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size with error handling"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """ instantiation with area """
    def area(self):
        return self.__size ** 2

    """ prints in stdout the square with character # """
    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for i in range(self.size):
                    print("#", end="")
                print("")
