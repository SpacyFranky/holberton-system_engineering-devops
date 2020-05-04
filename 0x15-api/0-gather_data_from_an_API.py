#!/usr/bin/python3
""" A Python script that, using a fake REST API, for a given employee ID,
    returns information about his/her TODO list progress
"""

import requests
import sys

if __name__ == '__main__':

    if len(sys.argv) == 2 and sys.argv[1].isdigit():

        f1 = 'todos?userId={}&completed=true'.format(sys.argv[1])
        f2 = 'todos?userId={}'.format(sys.argv[1])

        url_name = 'https://jsonplaceholder.typicode.com/users/{}'
        url_done_tasks = 'https://jsonplaceholder.typicode.com/{}'.format(f1)
        url_total_tasks = 'https://jsonplaceholder.typicode.com/{}'.format(f2)

        r_name = requests.get(url_name.format(sys.argv[1]))
        r_done_tasks = requests.get(url_done_tasks)
        r_total_tasks = requests.get(url_total_tasks)

        name = r_name.json().get("name")
        done = len(r_done_tasks.json())
        total = len(r_total_tasks.json())

        print("Employee {} is done with tasks({}/{}):".format(name, done,
                                                              total))
        l = r_done_tasks.json()
        for d in l:
            print("\t {}".format(d.get("title")))
