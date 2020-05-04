#!/usr/bin/python3
""" Dictionary of list of dictionaries  """

if __name__ == "__main__":
    import json
    from requests import get

    url_user = "https://jsonplaceholder.typicode.com/users"
    url_todo = "https://jsonplaceholder.typicode.com/todos"

    r_user = get(url_user)
    r_todo = get(url_todo)

    try:
        js_user = r_user.json()
        js_todo = r_todo.json()

    except ValueError:
        print("Not a valid JSON")

    if js_user and js_todo:
        data = {}
        user_names = {}
        for user in js_user:
            USER_ID = user.get('id')
            USERNAME = user.get('username')
            data[USER_ID] = []
            user_names[USER_ID] = USERNAME

        for todo in js_todo:
            TASK_COMPLETED_STATUS = todo.get("completed")
            TASK_TITLE = todo.get('title')
            user_id = todo.get("userId")
            dic = {"task": TASK_TITLE,
                   "completed": TASK_COMPLETED_STATUS,
                   "username": user_names.get(user_id)}

            if data.get(user_id) is not None:
                data.get(user_id).append(dic)

        with open('todo_all_employees.json', 'w', newline='') as jsonfile:
            json.dump(data, jsonfile)
