#!/usr/bin/python3
"""
Module containing class Base
"""

import json


class Base:
    """ class Base; tracks id """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor method """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes JSON string rep of list_objs to a file """
        list_obj = []
        filename = str(cls.__name__) + ".json"
        if list_objs is None:
            with open(filename, mode='w', encoding="utf-8") as f:
                f.write(cls.to_json_string(list_obj))
        else:
            for obj in list_objs:
                list_obj.append(cls.to_dictionary(obj))
            with open(filename, mode='w', encoding='utf-8') as f:
                f.write(cls.to_json_string(list_obj))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        json_list = []
        if json_string is None:
            return json_list
        if len(json_string) == 0:
            return json_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Square":
            dummy_cls = cls(1)
        elif cls.__name__ == "Rectangle":
            dummy_cls = cls(1, 1)
        dummy_cls.update(**dictionary)
        return dummy_cls

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        json_list = []
        instance_list = []
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                json_list = cls.from_json_string(f.read())
            for element in json_list:
                instance_list.append(cls.create(**element))
            return instance_list
        except FileNotFoundError:
            return json_list
