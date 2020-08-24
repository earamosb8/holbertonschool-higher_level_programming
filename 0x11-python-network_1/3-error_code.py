#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""

from urllib import request, error
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except error.URLError as e:
        print('Error code: {}'.format(e.code))
