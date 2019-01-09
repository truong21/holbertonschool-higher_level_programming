#!/usr/bin/python3
"""

Module containing print_square

"""


def print_square(size):
    """ Prints Square """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        pass
    else:
        for i in range(size):
            for i in range(size):
                print("#", end="")
            print("")
