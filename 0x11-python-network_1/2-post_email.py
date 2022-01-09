#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""

if __name__ == '__main__':
    import urllib.request as request
    import urllib.parse as parse
    from sys import argv

    url = 'http://63ef0617c0ac.c0cd6e92.hbtn-cod.io:5000/'
    value = {'email': '3507@holbertonschool.com'}

    data = parse.urlencode(value)
    data = data.encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
