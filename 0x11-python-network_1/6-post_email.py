#!/usr/bin/python3
"""
Module that sends a POST request to the passed URL with parameters
"""


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    r = requests.post(url, data = values)
    print(r.text)
