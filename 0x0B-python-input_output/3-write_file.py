#!/usr/bin/python3
"""
Module containing write_file function
"""


def write_file(filename="", text=""):
    """ writes a string to a text file and
        returns the number of characters written
    """
    lc = 0
    with open(filename, mode='w', encoding='utf-8') as f:
        nb_char = f.write(text)

    return nb_char
