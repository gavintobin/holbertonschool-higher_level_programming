#!/usr/bin/python3
"""0-read"""


def read_file(filename=""):
    """func"""
    with open('filename', encoding="utf-8") as f:
        print(f.read(), end='')
