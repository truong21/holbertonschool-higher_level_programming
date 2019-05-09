#!/usr/bin/python3
"""
Queries Reddit API and returns total number of suscribers
"""


import json
import requests


def number_of_subscribers(subreddit):
    """ return number of subscribers for a subreddit """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent': 'custom'}
    try:
        r = requests.get(url, headers=headers, allow_redirects=False).json()
        data_list = r.get("data")
        return (data_list.get('subscribers'))
    except Exception:
        return 0
