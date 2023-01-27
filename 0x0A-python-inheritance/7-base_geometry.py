#!/usr/bin/python3
class BaseGeometry:
    def __init__(self, area):
        self.area = area
        if not area:
            raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if not type(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
