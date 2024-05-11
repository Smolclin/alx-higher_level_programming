#!/usr/bin/python3
''' script that takes in a URL, sends a request to
the URL and displays the body of the response '''

import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    code_start = response.status_code
    if code_start > 400:
        print('Error code: {}'.format(code_start))
    else:
        print('{}'.format(response.text))
