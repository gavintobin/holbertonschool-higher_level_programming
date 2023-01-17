#!/usr/bin/python3
"""square class"""


class Square:
    """defines square class"""
    def __init__(self, size=0):
        """initializes square with size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
