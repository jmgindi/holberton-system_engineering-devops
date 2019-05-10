#!/usr/bin/python3
"""returns the number of subs to a subreddit"""

import requests


def number_of_subscribers(subreddit):
    """returns number of subscribers"""
    user = {"User-Agent": "Jack"}

    req = requests.get("https://www.reddit.com/r/{}/about.json"
                 .format(subreddit), headers=user)
    if req.status_code != requests.codes.ok:
        return 0
    else:
        return req.json().get("data").get("subscribers")
