#!/usr/bin/python3
"""
Module containing Class Square (inherits from Rectangle)
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ instantiation method """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Overloading the __str__ method """
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
            self.y, self.size))

    @property
    def size(self):
        """ getter for size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for size """
        self.__size = value
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updates attributes """
        sq_attr = ["id", "size", "x", "y"]
        if args:
            for index, value in enumerate(args):
                setattr(self, sq_attr[index], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    def to_dictionary(self):
        """ dictionary representation of a Square """
        self_dict = {'id': self.id, 'x': self.x, 'y': self.y, 
            'size' : self.size}
        return self_dict
