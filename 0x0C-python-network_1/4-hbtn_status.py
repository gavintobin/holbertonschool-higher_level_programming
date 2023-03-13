#!/usr/bin/python3
"""
Write a Python script that
takes in a URL and an email, sends
a POST request to the passed URL with
the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""
from urllib import request


if __name__ == '__main__':
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
 
    print('Body response:')
    print('\t- type:', type(html))
    print('\t- content:', html)
