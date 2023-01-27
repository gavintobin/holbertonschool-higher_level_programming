#!/usr/bin/python3
"""that tangy r"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """r tangs friend"""
    def __init__(self, size):
        size.integer_validator = ("size", size)
        super().__init__(size, size)
        self.__size = size
