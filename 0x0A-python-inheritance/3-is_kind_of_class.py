#!/usr/bin/python3
"""kindofclass"""


def is_kind_of_class(obj, a_class):
    "func"
    if isinstance(obj, a_class):
        return True
    if isinstance(obj, super(a_class)):
        return True
