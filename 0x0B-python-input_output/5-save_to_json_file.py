#!/usr/bin/python3
"""save json"""


def save_to_json_file(my_obj, filename):
    """func"""
    import json
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
