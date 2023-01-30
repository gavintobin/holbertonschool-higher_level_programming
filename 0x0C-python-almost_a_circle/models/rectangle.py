#!/usr/bin/python3
"""inherited from base"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            """retrieves the width"""
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) != int:
                raise TypeError('width must be an integer')
            if width <= 0:
                raise ValueError('width must be > 0')

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) != int:
                raise TypeError(' height must be an int')
            if height <= 0:
                raise ValueError('height must be > 0')

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            if type(value) != int:
                raise TypeError('x must be an integer')
            if x < 0:
                raise ValueError('x must be >= 0')

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            if type(value) != int:
                raise TypeError('y must be an integer')
            if y < 0:
                raise ValueError('y must be >= 0')
