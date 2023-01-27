#!/usr/bin/python3
"""inherits"""


def inherits_from(obj, a_class):
    """func"""
    if type(obj) != a_class and issubclass(type(obj, a_class)):
        return True
    return False
