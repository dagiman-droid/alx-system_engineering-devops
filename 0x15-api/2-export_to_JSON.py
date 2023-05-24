#!/usr/bin/python3
import json
import requests
from sys import argv


def export_tasks_to_json(user_id):
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    tasks = response.json()

    user_tasks = []
    for task in tasks:
        if task["userId"] == int(user_id):
            user_tasks.append({
                "task": task["title"],
                "completed": task["completed"],
                "username": task["username"]
            })

    data = {user_id: user_tasks}
    file_name = f"{user_id}.json"
    with open(file_name, "w") as json_file:
        json.dump(data, json_file)

# Get the user_id from the command line argument
user_id = argv[1]

export_tasks_to_json(user_id)

