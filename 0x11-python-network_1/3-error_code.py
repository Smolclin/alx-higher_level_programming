#!/usr/bin/python3
''' Python script that takes in a URL, sends a request to
the URL and displays the body of the response '''

from urllib import parse, error, request
import sys

if __name__ == '__name__':
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
