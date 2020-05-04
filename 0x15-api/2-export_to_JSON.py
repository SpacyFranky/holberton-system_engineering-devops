#!/usr/bin/python3
""" A Python script that exports data in the JSON format """

import json
import requests
import sys

if __name__ == '__main__':

    if len(sys.argv) == 2 and sys.argv[1].isdigit():

        f = 'todos?userId={}'.format(sys.argv[1])

        url_username = 'https://jsonplaceholder.typicode.com/users/{}'
        url_todo = 'https://jsonplaceholder.typicode.com/{}'.format(f)

        r_username = requests.get(url_username.format(sys.argv[1]))
        r_todo = requests.get(url_todo)

        username = r_username.json().get("username")
        l = r_todo.json()
        data = {sys.argv[1]: []}
        for d in l:
            add = {}
            add['task'] = d.get("title")
            add['completed'] = d.get("completed")
            add['username'] = username
            data[sys.argv[1]].append(add)
        with open('{}.json'.format(sys.argv[1]), 'w', newline='') as file:
            json.dump(data, file)
