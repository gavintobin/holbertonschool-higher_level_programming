#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        size.integer_validator = ("size", size)

    def area(self):
        return self.__size * 2
