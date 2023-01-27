#!/usr/bin/python3
"""mylist"""


class MyList(list):
    """mylist"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
