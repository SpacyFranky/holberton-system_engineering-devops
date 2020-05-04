#!/usr/bin/python3
""" A Python script that exports data in the CSV format """

import csv
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
        with open('{}.csv'.format(sys.argv[1]), 'w', newline='') as csvfile:
            for d in l:
                writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
                writer.writerow([sys.argv[1], username, d.get("completed"),
                                 d.get("title")])
