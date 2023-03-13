#!/usr/bin/python3
"""HBTN Status"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.argv[2]
    req = requests.get(url, auth=HTTPBasicAuth(username, token)).json()
    print(req.get('id'))
