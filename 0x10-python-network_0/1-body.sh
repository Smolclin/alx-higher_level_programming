#!/bin/bash
# cript that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sLGET "$1"
