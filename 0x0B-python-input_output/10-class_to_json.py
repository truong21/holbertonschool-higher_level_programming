#!/usr/bin/python3
"""
Module containing class_to_json function
"""


def class_to_json(obj):
    """ returns a dictionary description with simple data structure """
    return obj.__dict__
