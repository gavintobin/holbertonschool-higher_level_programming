#!/usr/bin/python3
"""
Write a Python script that
takes in a URL and an email, sends
a POST request to the passed URL with
the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""


if __name__ == '__main__':
    import requests
    req = requests.get('https://intranet.hbtn.io/status')
 
    print('Body response:')
    print('\t- type:', type(req.text))
    print('\t- content:', req.text)
