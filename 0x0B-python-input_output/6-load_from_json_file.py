#!/usr/bin/python3
import json
"""fromjson"""


def load_from_json_file(filename):
    """func"""
    with open(filename) as f:
        return json.load(f)
