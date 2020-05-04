#!/usr/bin/python3
""" Export to CSV  """

if __name__ == "__main__":
    from requests import get
    from sys import argv, exit
    import csv

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

        with open(id + '.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_ALL)
            for todo in js_todo:
                TASK_COMPLETED_STATUS = todo.get("completed")
                TASK_TITLE = todo.get('title')
                spamwriter.writerow([USER_ID,
                                     USERNAME,
                                     TASK_COMPLETED_STATUS,
                                     TASK_TITLE])
