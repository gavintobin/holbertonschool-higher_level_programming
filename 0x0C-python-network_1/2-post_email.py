#!/usr/bin/python3
"""
proj task 2 Write a Python script that takes
in a URL and an email, sends a POST request to
the passed URL with the email as a parameter
and displays the body of the response (decoded in
utf-8)
"""
import sys
from urllib import request, parse


def send_post_request(url, email):
    """post request function"""
    data = parse.urlencode({'email': email}).encode('utf-8')
    with request.urlopen(url, data) as response:
        return response.read().decode('utf-8')


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    response_body = send_post_request(url, email)
    print('your email is {}'.format(email))
