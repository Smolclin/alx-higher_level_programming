#!/usr/bin/python3
''' script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter '''

import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    arg_len = len(sys.argv)
    if arg_len == 2:
        q_1 = sys.argv[1]
    else:
        q_1 = ""
    req = requests.post(url, data={'q_1': q_1})
    try:
        req = req.json()
        if not req:
            print('No result')
        else:
            print('[{}] {}'.format(req['id'], req['name']))
    except ValueError:
        print('Not a valid')
