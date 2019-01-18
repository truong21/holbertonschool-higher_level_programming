#!/usr/bin/python3
"""
Module containing write_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object string to a text file using JSON rep """
    lc = 0
    with open(filename, mode='w') as f:
        f.write(json.dumps(my_obj))
