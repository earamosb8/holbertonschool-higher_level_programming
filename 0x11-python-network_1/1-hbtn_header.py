#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""


import sys
import urllib.request

with urllib.request.urlopen(sys.argv[1]) as html:
    print(html.headers['X-Request-Id'])
