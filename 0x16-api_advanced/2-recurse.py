#!/usr/bin/python3
"""This file contains a function that queries the Reddit API
   and returns a list containing the titles of all hot articles for
   a given subreddit. If no results are found for the given subreddit,
   the functio returns None.
"""

import requests


# Iterative Method

#def recurse(subreddit):
    #"""returns a list containing the titles of all hot articles
    #   for a given subreddit.
    #   if no results are found, it returns None.
    #"""

    #url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(subreddit)
    #r = requests.get(url, headers={'User-agent': 'hello-student 0.4'})
    #hot = r.json()
    #l = []
    #v = 0
    #while (v == 0):
    #    l.extend(hot.get('data').get('children'))
    #    if hot.get('data').get('after') is None:
    #        v = 1
    #    f = '?limit=100&after={}'.format(hot.get('data').get('after'))
    #    url = 'https://www.reddit.com/r/{}/hot.json{}'.format(subreddit, f)
    #    r = requests.get(url, headers={'User-agent': 'hello-student 0.4'})
    #    hot = r.json()
    #return l

# Recursive Method

def recurse(subreddit, hot_list=[]):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = requests.get(url, headers={'User-Agent': 'hello-student 0.4'},
                     params={'limit': 100})
    d = r.json()
    try:
        for i in d['data']['children']:
            if i['data']['title'] == [] or i['data']['title'] is None:
                return hot_list
            hot_list.append(i['data']['title'])
        name = d['data']['after']
        if d['data']['after'] is None:
            return
    except KeyError:
        return None
    recurse_helper(subreddit, hot_list, name)
    return hot_list


def recurse_helper(subreddit, hot_list=[], name=""):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = requests.get(url, headers={'User-Agent': 'hello-student 0.4'},
                     params={'after': name, 'limit': 100})
    d = r.json()
    try:
        for i in d['data']['children']:
            if i['data']['title'] == [] or i['data']['title'] is None:
                return hot_list
            hot_list.append(i['data']['title'])
        if d['data']['after'] is None:
            return
    except KeyError:
        return None
    return recurse_helper(subreddit, hot_list, d['data']['after'])
