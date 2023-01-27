#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    if isinstance(obj, super(a_class)):
        return True
