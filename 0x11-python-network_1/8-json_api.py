#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests


if __name__ == '__main__':
    if len(argv[1]) == 0:
        q = ""
    else:
        q = argv[1]

    data = {'q': q}
    request = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        json = request.json()
        if len(json) == 0 or not json['id'] or not json['name']:
            print("No result")
        else:
            print("[{}] {}".format(json['id'], json['name']))
    except:
        print("Not a valid JSON")
