#!/usr/bin/python3
def add_integer(a, b=98):
    if a or b is not type(int):
        raise TypeError('a must be an integer'/ 'b must be integer')
    if a is type(float):
        a = int(a)
    if b is type(float):
        b = int(b)
        return a + b
