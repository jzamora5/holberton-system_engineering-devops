#!/usr/bin/python3
""" Recurse it! """
from requests import get


def recurse(subreddit, hot_list=[], after=""):
    """
     returns a list containing the titles of all hot articles for a given
    subreddit. If no results are found for the given subreddit, the function
    should return None.
    """
    if after == None:
        return hot_list


    test_list = []

    headers = {'user-agent': 'my-app/0.0.1'}
    red = "https://www.reddit.com/"

    after = ""

    while(after != None):

        url = red + "r/{}/hot/.json?limit=100&after={}".format(subreddit, after)

        r = get(url, headers=headers, allow_redirects=False)

        if r.status_code != 200:
            return None

        try:
            js = r.json()

        except ValueError:
            return None

        try:

            data = js.get("data")
            after = data.get("after")
            children = data.get("children")
            for child in children:
                post = child.get("data")
                test_list.append(post.get("title"))

        except:
            print(None)

    return test_list
