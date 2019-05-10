#!/usr/bin/python3
"""contains 1 function: top_ten"""

import requests


def top_ten(subreddit):
    """returns the top 10 hot posts of a subreddit"""
    user = {"User-Agent": "Jack"}
    req = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit), headers=user)
    if req.status_code is not requests.codes.ok or \
       len(req.json().get("data").get("children")) is 0:
        print("None")
        return 0
    for i in range(10):
        print(req.json()
              .get("data").get("children")[i].get("data").get("title"))
