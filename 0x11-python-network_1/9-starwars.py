#!/usr/bin/python3
"""
Module containing script that takes in a string and sends a search request
to the Star Wars API
"""


import requests
import sys


if __name__ == "__main__":
    url = 'https://swapi.co/api/people/'
    try:
        word = sys.argv[1]
    except Exception:
        word = ""

    payload = {'search': word}
    r = requests.get(url, params=payload)
    json_to_dict = dict(r.json())
    print("Number of results: {}".format(json_to_dict.get('count')))

    dict_results = json_to_dict.get('results')
    for res in dict_results:
        for key, value in res.items():
            if key == 'name':
                print(value)
