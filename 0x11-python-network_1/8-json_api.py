#!/usr/bin/python3
"""
Write a Python script that
takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
from os import sys
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    response = requests.post(url, data={'q': q})
    try:
        if len(response.json()) == 0:
            print('No result')
        else:
            info = response.json()
            print("[{}] {}".format(info['id'], info['name']))
    except:
        print('Not a valid JSON')
