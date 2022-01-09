#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

import urllib.request as request
import urllib.error as HTTPError
from sys import argv


if __name__ == '__main__':
    try:
        with request.urlopen(argv[1]) as r:
            print(r.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
