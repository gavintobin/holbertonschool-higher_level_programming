#!/usr/bin/python3
BaseGeometry = __import__('8-rectangle').Basegeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validation("width", width)
        self.integer_validation("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        print('[Rectangle {}/{}'.format(self.__width, self.__height))
