#!/usr/bin/python3
"""
Module containing script that takes your Github credentials
(username and password) and uses the Github API to display your id
"""


import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    passwd = sys.argv[2]

    r = requests.get(url, auth=(username, passwd))
    r_json = r.json()
    try:
        print(r_json['id'])
    except Exception:
        print("None")
