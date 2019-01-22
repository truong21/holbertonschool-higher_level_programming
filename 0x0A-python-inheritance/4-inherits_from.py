#!/usr/bin/python3
"""
Module containing inherits_from function"
"""


def inherits_from(obj, a_class):
    """ function that returns True if the object is an instance of a class
        that inherited(directly or indirectly) from, the specific class ;
        otherwise False """
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
