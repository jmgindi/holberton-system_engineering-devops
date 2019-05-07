#!/usr/bin/python3
"""gathers completed tasks for an employee from API"""

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        exit(1)

    user = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    name = requests.get(user).json().get('name')
    req = "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1]
    request = requests.get(req)
    f_name = argv[1] + ".json"

    with open(f_name, 'w') as f:
        d = {argv[1]: []}
        for r in request.json():
            d.get(argv[1]).append({
                "task": r.get('title'),
                "completed": r.get('completed'),
                "username": name})
        json.dump(d, f)
