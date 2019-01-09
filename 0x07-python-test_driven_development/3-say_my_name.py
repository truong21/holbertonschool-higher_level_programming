#!/usr/bin/python3
"""

Module containing say_my_name

"""


def say_my_name(first_name, last_name=""):
    """ prints the name """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if len(first_name) == 0:
        print("My name is {:s}".format(last_name))
    elif len(last_name) == 0:
        print("My name is {:s}".format(first_name))
    elif len(first_name) == 0 and len(last_name) == 0:
        print("My name is")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
