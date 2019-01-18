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

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a student instance """
        all_string = True
        if isinstance(attrs, list):
            for elem in attrs:
                if not isinstance(elem, str):
                    all_string = False
                    break
        else:
            all_string = False

        if all_string is True:
            stu_dict = {}
            for elem in attrs:
                if elem in self.__dict__:
                    stu_dict[elem] = self.__dict__[elem]
            return stu_dict
        return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of the student stance from json """
        for key in json.keys():
            self.__dict__[key] = json[key]
