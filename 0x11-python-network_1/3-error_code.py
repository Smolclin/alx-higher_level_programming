#!/usr/bin/python3
''' Python script that takes in a URL, sends a request to
the URL and displays the body of the response '''

from urllib import request, error
import requests

if __name__ == '__name__':
    url = sys.argv[1]

    my_req = request.Request(url)
    try:
        with request.urlopen(my_req) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
