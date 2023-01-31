#!/usr/bin/python3
"""square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, kid=None):
        super().__init__(id, x, y)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """rets sqr info"""
        r = "[Square] " + "({}) ".format(self.id)
        r += "{}/{} - ".format(self.x, self.y)
        r += "{}".format(self.width)
        return r
