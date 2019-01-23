#!/usr/bin/python3
"""
Class Rectangle(inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle """
    def __init__(self, width, height):
        """ instantiation of a rectangle """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ string representation """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
