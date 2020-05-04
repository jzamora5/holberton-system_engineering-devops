#!/usr/bin/python3
""" Export to JSON  """

if __name__ == "__main__":
    import json
    from requests import get
    from sys import argv, exit

    try:
        id = argv[1]
        is_int = int(id)
    except:
        exit()

    url_user = "https://jsonplaceholder.typicode.com/users?id=" + id
    url_todo = "https://jsonplaceholder.typicode.com/todos?userId=" + id

    r_user = get(url_user)
    r_todo = get(url_todo)

    try:
        js_user = r_user.json()
        js_todo = r_todo.json()

    except ValueError:
        print("Not a valid JSON")

    if js_user and js_todo:
        USER_ID = id
        USERNAME = js_user[0].get('username')

        js_list = []
        for todo in js_todo:
            TASK_COMPLETED_STATUS = todo.get("completed")
            TASK_TITLE = todo.get('title')

            dic = {"task": TASK_TITLE,
                   "completed": TASK_COMPLETED_STATUS,
                   "username": USERNAME}

            js_list.append(dic)

        data = {USER_ID: js_list}

        with open(id + '.json', 'w', newline='') as jsonfile:
            json.dump(data, jsonfile)
