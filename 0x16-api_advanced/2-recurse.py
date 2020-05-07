#!/usr/bin/python3
"""This file contains a function that queries the Reddit API
   and returns a list containing the titles of all hot articles for
   a given subreddit. If no results are found for the given subreddit,
   the functio returns None.
"""

import requests


def recurse(subreddit):
    """returns a list containing the titles of all hot articles
       for a given subreddit.
       if no results are found, it returns None.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(subreddit)
    r = requests.get(url, headers={'User-agent': 'hello-student 0.4'})
    hot = r.json()
    l = []
    v = 0
    while (v == 0):
        l.extend(hot.get('data').get('children'))
        if hot.get('data').get('after') is None:
            v = 1
        f = '?limit=100&after={}'.format(hot.get('data').get('after'))
        url = 'https://www.reddit.com/r/{}/hot.json{}'.format(subreddit, f)
        r = requests.get(url, headers={'User-agent': 'hello-student 0.4'})
        hot = r.json()
    return l
