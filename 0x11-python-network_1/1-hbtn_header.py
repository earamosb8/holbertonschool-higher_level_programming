#!/usr/bin/python3
import sys
import urllib.request

"""script that fetches https://intranet.hbtn.io/status"""

with urllib.request.urlopen(sys.argv[1]) as html:
    print(html.headers['X-Request-Id'])
