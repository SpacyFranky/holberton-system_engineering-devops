#!/usr/bin/python3
""" A Python script that exports data in the JSON format """

import json
import requests
import sys
from collections import OrderedDict

if __name__ == '__main__':

    url_users = 'https://jsonplaceholder.typicode.com/users'
    u_users = requests.get(url_users)
    users = u_users.json()

    data = OrderedDict()

    for i in range(1, len(users) + 1):

        f = 'todos?userId={}'.format(i)

        url_username = 'https://jsonplaceholder.typicode.com/users/{}'
        url_todo = 'https://jsonplaceholder.typicode.com/{}'.format(f)

        r_username = requests.get(url_username.format(i))
        r_todo = requests.get(url_todo)

        username = r_username.json().get("username")
        l = r_todo.json()

        data[str(i)] = []

        for d in l:
            add = OrderedDict()
            add['username'] = username
            add['task'] = d.get("title")
            add['completed'] = d.get("completed")
            data[str(i)].append(add)

    with open('todo_all_employees.json', 'w', newline='') as file:
        json.dump(data, file)
