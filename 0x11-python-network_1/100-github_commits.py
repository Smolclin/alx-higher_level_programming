#!/usr/bin/python3
''' script that takes 2 arguments in order to solve a challenge '''
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    req = requests.get(url)
    commits = req.json()
    try:
        for g in range(10):
            print("{}: {}".format(
                commits[g].get("sha"),
                commits[g].get("commit").get("author").get("name")))
    except IndexError:
        pass
