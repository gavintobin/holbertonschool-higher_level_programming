#!/usr/bin/python3
"""inherited from base"""
from models.base import Base


class Rectangle(Base):
    """subclass of base"""

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
            """sets width val for rectangle"""
            if type(value) != int:
                raise TypeError('width must be an integer')
            if width <= 0:
                raise ValueError('width must be > 0')
            self.__width = value

        @property
        def height(self):
            """gets height for rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            """sets height val for rectangle"""
            if type(value) != int:
                raise TypeError(' height must be an int')
            if height <= 0:
                raise ValueError('height must be > 0')
            self.__height = value

        @property
        def x(self):
            """gets x val for rectangle"""
            return self.__x

        @x.setter
        def x(self, value):
            """sets val of x in rectangle"""
            if type(value) != int:
                raise TypeError('x must be an integer')
            if x < 0:
                raise value

        @property
        def y(self):
            """returns val of ractangle"""
            return self.__y

        @y.setter
        def y(self, value):
            """sets y val of rectangle"""
            if type(value) != int:
                raise TypeError('y must be an integer')
            if y < 0:
                raise ValueError('y must be >= 0')
            self.__y = value

        def area(self):
            """ gets value of area for rec"""
            return self.__height * self.__width

        def display(self):
            """printts rectangle to stdout"""
            r = '\n' * self.y
            r += (' ' * self.x + '#' * self.width + '\n')
            r = r[:-1]
            print(r)

        def __str__(self):
            """returns string output of rec"""
            return '[' + type(self.__name__) + ']' + '(' + str(self.__id) \
                + ')' + str(self.__x) + '/' + str(self.__y) + '-' \
                + str(self.__width) + '/' + str(self.__height)
