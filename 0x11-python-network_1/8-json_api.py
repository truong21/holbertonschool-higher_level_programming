#!/usr/bin/python3
"""
Module containing script that do POST request to site
with a letter as a parameter
"""


import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    try:
        letter = sys.argv[1]
    except Exception:
        letter = ""

    parameters = {'q': letter}
    r = requests.post(url, data=parameters)
    try:
        res = r.json()
        if 'id' in res:
            json_id = res.get('id')
            json_name = res.get('name')
            print("[{}] {}".format(json_id, json_name))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
