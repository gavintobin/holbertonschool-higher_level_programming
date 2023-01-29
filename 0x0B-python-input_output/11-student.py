#!/usr/bin/python3
"""class"""


class Student:
    """func"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) == list:
            if all(type(attrs) == str for attr in attrs):
                return {att: getattr(self, att)
                        for att in attrs if hasattr(self, att)}
        else:
            return self.__dict__

        def reload_from_json(self, json):
            for k, v in json.items():
                setattr(self, k, v)
