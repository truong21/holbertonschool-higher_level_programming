#!/usr/bin/python3
"""

Module containing matrix_divided functions

"""


def matrix_divided(matrix, div):
    """ function that divides all elements of a matrix """
    s = "matrix must be a matrix (list of lists) of integers/floats"
    if not (isinstance(div, float) or isinstance(div, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError(s)
    if len(matrix) == 0:
        raise TypeError(s)
    for row in matrix:
        if len(row) == 0:
            raise TypeError(s)
        for num in row:
            if not (isinstance(num, int) or isinstance(num, float)):
                raise TypeError(s)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    return [[round((num / div), 2) for num in row] for row in matrix]
