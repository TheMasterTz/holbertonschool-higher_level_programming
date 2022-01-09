#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id.
"""
from sys import argv
import requests


if __name__ == '__main__':

    r = requests.get('https://api.github.com/user', data = (argv[1], argv[2]))
    r = r.json()
    print(r.get('id'))