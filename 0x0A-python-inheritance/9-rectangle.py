#!/usr/bin/python3
""" dat base g boiiii"""
BaseGeometry = __import__('8-rectangle').BaseGeometry


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
