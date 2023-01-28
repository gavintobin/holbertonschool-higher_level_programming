#!/usr/bin/python3
"""json"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    """func"""
    try:
        loadr = load_from_json_file("add_item.json")
    except FileNotFoundError:
        loadr = []
        loadr.extend(sys.argv[1:])
        save_to_json_file(loadr, "add_item.json")
