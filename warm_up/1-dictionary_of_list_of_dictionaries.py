#!/usr/bin/python3
"""
script to return information about all employees' TODO list progress in JSON
"""

if __name__ == '__main__':
    import json
    import requests

    try:
        user_r = requests.get('http://jsonplaceholder.typicode.com/users')
        todos_r = requests.get('http://jsonplaceholder.typicode.com/todos')
    except Exception as e:
        print(e)
        raise
    users = user_r.json()
    todos = todos_r.json()
    usernames = {}
    tasks = {}
    for user in users:
        user_id = user.get('id', None)
        username = user.get('username', None)
        if user_id is not None and username is not None:
            usernames[user_id] = username
            tasks[user_id] = []
    for task in todos:
        user_id = task.get('userId', None)
        title = task.get('title', None)
        completed = task.get('completed', None)
        username = usernames.get(user_id, None)
        if user_id is not None and title is not None and completed is not \
           None and username is not None:
            task_info = {}
            task_info['username'] = username
            task_info['task'] = title
            task_info['completed'] = completed
            tasks[user_id].append(task_info)
    with open('todo_all_employees.json', 'w+') as f:
        json.dump(tasks, f)
