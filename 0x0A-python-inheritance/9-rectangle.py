#!/usr/bin/python3
"""rectang"""


class BaseGeometry:
    """class"""
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """r tang m'baby """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validation("width", width)
        self.integer_validation("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        rstr = "[Rectangle]"
        rstr += str(self.__width) + "/" + str(self.__height)
        return rstr
