import json

def export_tasks_to_json(user_id, tasks):
    data = {user_id: []}
    for task in tasks:
        data[user_id].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": task["username"]
        })
    
    file_name = f"{user_id}.json"
    with open(file_name, "w") as json_file:
        json.dump(data, json_file)

# Example usage
user_id = "USER123"
tasks = [
    {"title": "Task 1", "completed": False, "username": "John"},
    {"title": "Task 2", "completed": True, "username": "John"},
    {"title": "Task 3", "completed": True, "username": "John"},
    {"title": "Task 4", "completed": False, "username": "John"}
]

export_tasks_to_json(user_id, tasks)

