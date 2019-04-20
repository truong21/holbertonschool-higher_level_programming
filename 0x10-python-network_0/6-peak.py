#!/usr/bin/python3
"""
Module containing find_peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers """
    if not list_of_integers:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    peak = list_of_integers[0]
    for x in range(len(list_of_integers) - 1):
        if list_of_integers[x + 1] > list_of_integers[x]:
            peak = list_of_integers[x + 1]
        elif list_of_integers[x] > list_of_integers[x + 1]:
            peak = list_of_integers[x]
    return peak
