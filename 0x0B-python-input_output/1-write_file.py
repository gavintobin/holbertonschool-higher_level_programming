#!/usr/bin/python3
"""write file"""


def write_file(filename="", text=""):
    """func"""
    with open(filename, encoding="utf-8") as f:
        f.write(text)
    return len(text)
