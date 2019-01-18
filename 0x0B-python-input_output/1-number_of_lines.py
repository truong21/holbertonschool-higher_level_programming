#!/usr/bin/python3
"""
Module containing number_of_line function
"""


def number_of_lines(filename=""):
    """ reads a text file and returns the number of lines """
    lc = 0
    with open(filename) as f:
        for line in f:
            lc += 1
    return lc
