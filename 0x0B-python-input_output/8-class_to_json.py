#!/usr/bin/python3
"""json"""


def class_to_json(obj):
    """func"""
    mydict = {}
    for k, v in obj.__dict__.items():
        if isinstance(v, (int, bool, str, list, dict)):
            mydict[k] = v
    return mydict
