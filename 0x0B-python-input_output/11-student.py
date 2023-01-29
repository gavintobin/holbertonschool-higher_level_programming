#!/usr/bin/python3
"""class"""


class Student:
    """func"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        mydict = vars(self)
        if attrs is None:
            return mydict

        student = {}
        for i in attrs:
            if i in mydict:
                student[i] = mydict[i]
        return student

    def reload_from_json(self, json):
        self.__dict__.update(json)
