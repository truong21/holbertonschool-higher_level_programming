#!/usr/bin/python3
"""
Module containing read_file function
"""


def read_file(filename=""):
    """ reads a text file and prints it to stdout """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
