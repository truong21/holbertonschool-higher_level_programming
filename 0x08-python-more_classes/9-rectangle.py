#!/usr/bin/python3
"""

Module Containing class Rectangle

"""


class Rectangle:
    """ Rectangle Class with width and height attribute """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initializes a rectangle with width and height """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ retrieves width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width with error handling """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieves height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the width with error handling """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ public instantiation of area """
        return self.__height * self.__width

    def perimeter(self):
        """ public instantiation of perimeter """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ string representation of a rectangle """
        s = ""
        if self.__height == 0 or self.__width == 0:
            return s
        for x in range(self.__height):
            for y in range(self.__width):
                s += str(self.print_symbol)
            if x != self.__height - 1:
                s += "\n"
        return s

    def __repr__(self):
        """ string representation for an instance of a rectangle """
        w = str(self.__width)
        h = str(self.__height)
        return "Rectangle(" + w + ", " + h + ")"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ static method that returns the biggest rectangle based on area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ returns a new Rectangle instance with height == width """
        return Rectangle(size, size)

    def __del__(self):
        """ destruction of a rectangle instance """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
