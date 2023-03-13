#!/usr/bin/python3
"""
u hoh error code Write a Python script that takes
in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the
header of the response.
"""
from urllib import request, error
import sys

if __name__ == '__main__':

    url = sys.argv[1]
    http = request.Request(url)

    try:
        with request.urlopen(http) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
