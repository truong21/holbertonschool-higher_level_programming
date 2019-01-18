#!/usr/bin/python3
"""
Class Student
"""


class Student:
    """ Defines class Student """
    def __init__(self, first_name, last_name, age):
        """ initiates attributes for student instance """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation of a student instance """
        return self.__dict__
