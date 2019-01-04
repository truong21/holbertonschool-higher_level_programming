#!/usr/bin/python3
"""
Class Square: contains optional size, area
"""


class Square:
    """Create an square with private instance attribute: size and position"""
    def __init__(self, size=0, position=(0, 0)):
        """ initializes a square with attributes """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ retrieves the size """
        return self.__size

    @property
    def position(self):
        """ retrieves the size """
        return self.__position

    @size.setter
    def size(self, value):
        """ sets the size with error handling"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """ sets the position with error handling """
        err = "position must be a tuple of 2 positive integers"
        if type(value) is tuple:
            if len(value) != 2:
                raise TypeError(err)
            for i in range(len(value)):
                if value[i] < 0:
                    raise TypeError(s)
            self.__position = value

    """ instantiation with area """
    def area(self):
        return self.__size ** 2

    """ prints in stdout the square with character # """
    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for num in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for i in range(self.__size + self.__position[0]):
                    if i < self.__position[0]:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print("")
