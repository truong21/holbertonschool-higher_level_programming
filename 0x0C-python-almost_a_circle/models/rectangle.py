#!/usr/bin/python3
"""
Module containing Class Rectangle (inherits from Base)
"""


from models.base import Base


class Rectangle(Base):
    """
    class Rectangle:
    args:
        (int) width
        (int) height
        (int) x
        (int) y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ instantiation method """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ retrieves width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width with error handling """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ retrieves height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the width with error handling """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ retrieves position x """
        return self.__x

    @x.setter
    def x(self, value):
        """ sets the x positin of the rectangle """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ retrieves position y """
        return self.__y

    @y.setter
    def y(self, value):
        """ sets the y positin of the rectangle """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area of rectangle """
        return self.__height * self.__width

    def display(self):
        """ prints in stdout the Rectangle instance with '#' """
        for row1 in range(self.__y):
            print("")
        for row2 in range(self.__height):
            for column1 in range(self.__x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """ Overriding the __str__ method """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        attr = ["id", "width", "height", "x", "y"]
        if args:
            for index, value in enumerate(args):
                setattr(self, attr[index], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ dictionary representation of a Rectangle """
        self_dict = dict(self.__dict__)
        for key in self_dict:
            new_key = key.replace("_Rectangle__", "")
            self_dict[new_key] = self_dict.pop(key)
        return self_dict
