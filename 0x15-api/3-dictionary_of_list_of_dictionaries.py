#!/usr/bin/python3
"""gathers completed tasks for all employees from API to JSON file"""

import json
import requests


if __name__ == "__main__":
    length = len(requests.get(
        "https://jsonplaceholder.typicode.com/users").json())
    f_name = "todo_all_employees.json"

    all_todo = {}
    
    with open(f_name, 'w') as f:
        for user in range(1, length + 1):
            u = requests.get(
                "https://jsonplaceholder.typicode.com/users/"
                + str(user))
            name = u.json().get('username')
            all_todo[user] = []
            url = "https://jsonplaceholder.typicode.com/todos?" + str(user)
            r = requests.get(url)
            for task in r.json():
                all_todo[user].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": name})
        json.dump(all_todo, f)
