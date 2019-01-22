#!/usr/bin/python3
"""
Module containing is_kind_of_class function"
"""


def is_kind_of_class(obj, a_class):
    """ function that returns True if the object is exactly an instance of a 
        class that inherited from, the specific class ; otherwise False """
    return isinstance(obj, a_class)
