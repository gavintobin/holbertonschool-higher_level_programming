#!/usr/bin/python3
import sys
import urllib.request

if __name__ == '__main__':

    url = sys.argv[1]

with urllib.request.urlopen(url) as resp:
    head = resp.info()
    x_request_id = head['X-request-Id']
    print(x_request_id)
