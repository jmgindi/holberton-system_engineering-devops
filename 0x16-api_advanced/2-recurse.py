#!/usr/bin/python3
"""contains 1 function, recurse"""
import requests


def recurse(subreddit, hot_list=[]):
    """returns a list containing all hot articles"""
    user = {"User-Agent": "Jack"}
    if len(hot_list) is 0:
        req = requests.get("https://www.reddit.com/r/{}/hot.json"
                           .format(subreddit), headers=user)
    else:
        req = requests.get("https://www.reddit.com/r/{}/hot.json"
                           .format(subreddit) + "?after={}_{}"
                           .format(hot_list[-1].get("kind"),
                                   hot_list[-1].get("data").get("id")),
                           headers=user)
    if req.status_code is not requests.codes.ok:
        return None
    if len(req.json().get("data").get("children")) < 1:
        return hot_list
    hot_list.extend(req.json().get("data").get("children"))
    return recurse(subreddit, hot_list)
