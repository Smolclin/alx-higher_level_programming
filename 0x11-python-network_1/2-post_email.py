#!/usr/bin/python3
''' Python script that takes in a URL and an email, sends
a POST request to the passed URL with the email as a parameter '''

from urllib import request, parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    value = parse.urlencode(value).encode('utf-8')
    req = request.Request(url, value)

    with request.urlopen(req) as response:
        r_page = response.read().decode('utf-8')
        print(r_page)
