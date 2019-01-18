#!/usr/bin/python3
"""
Module containing load_from_json_file function
"""
import json


def load_from_json_file(filename):
    """ creates an Object from a JSON file """
    with open(filename, mode='r') as f:
        return json.load(f)
