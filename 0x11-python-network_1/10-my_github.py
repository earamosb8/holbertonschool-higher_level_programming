#!/usr/bin/python3
"""
Write a Python script that takes your Github
credentials (username and password) and uses
the Github API to display your id
"""
from os import sys
import requests

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    token = sys.argv[2]

    response = requests.get(url, auth=(user, token))
    js = response.json()
    try:
        print(js['id'])
    except KeyError:
        print('None')
