#!/usr/bin/python3
"""
Module containing find_peak
"""


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers """
    if type(list_of_integers) is not list:
        return None
    if len(list_of_integers) < 1:
        return None
    length = len(list_of_integers)
    peak = list_of_integers[0]
    for num in list_of_integers:
        if length == 1:
            return peak
        if num < peak:
            return peak
        if num > peak:
            peak == num
    return peak
