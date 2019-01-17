#!/usr/bin/python3
"""
Module containing read_line function
"""


def read_lines(filename="", nb_lines=0):
    """ reads n lines of text file and prints it to stdout """
    lc = 0
    with open(filename, encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        for line in f:
            if lc < nb_lines:
                print(line, end="")
                lc += 1
