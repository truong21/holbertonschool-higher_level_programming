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
