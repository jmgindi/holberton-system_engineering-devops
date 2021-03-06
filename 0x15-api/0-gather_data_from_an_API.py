#!/usr/bin/python3
"""gathers completed tasks for an employee from API"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        exit(1)

    user = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    name = requests.get(user).json().get('name')
    req = "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1]
    request = requests.get(req)

    total = [task for task in request.json()]
    completed = [task for task in request.json() if task.get('completed')]

    print(
        "Employee {} is done with tasks ({}/{}):"
        .format(name, len(completed), len(total)))
    for task in completed:
        print("\t {}".format(task.get('title')))
