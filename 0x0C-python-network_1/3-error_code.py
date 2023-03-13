#!/usr/bin/python3
"""HBTN Status"""
from urllib import request, parse, error
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
