#!/usr/bin/python3
"""ractang"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """skware"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        s = "[Square] "
        s += str(self.__size) + "/" + str(self.__size)
        return s
