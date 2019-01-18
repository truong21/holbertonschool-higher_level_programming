#!/usr/bin/python3
"""
Module containing pascal_triangle function
"""


def pascal_triangle(n):
    """ returns a list of lists of integers representing the Pascal's
        triangle of n """
    if n <= 0:
        return []
    result = []
    for i in range(n):
        result.append([])
        result[i].append(1)
        for j in range(1, i):
            result[i].append(result[i - 1][j - 1]+result[i-1][j])
        if n != 0 and i != 0:
            result[i].append(1)
    return result
