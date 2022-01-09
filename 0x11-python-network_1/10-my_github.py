#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id.
"""
from sys import argv
import requests


if __name__ == '__main__':

    auth = (argv[1], argv[2])
    response = requests.get('https://api.github.com/user', data = auth).json()
    print(response.get('id'))