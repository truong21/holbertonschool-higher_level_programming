#!/usr/bin/python3
"""
Module containing append_write function
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8) and
    returns the number of characters added
    """
    lc = 0
    with open(filename, mode='a', encoding='utf-8') as f:
        nb_char = f.write(text)

    return nb_char
