#!/usr/bin/python3
""" Count it! """
from requests import get

REDDIT = "https://www.reddit.com/"
HEADERS = {'user-agent': 'my-app/0.0.1'}


def count_words(subreddit, word_list, after=""):
    """
    Returns a list containing the titles of all hot articles for a
    given subreddit. If no results are found for the given subreddit,
    the function should return None.
    """
    if after == "":
        word_list = [[w.lower(), 0] for w in word_list]

    if after is None:
        word_list = sorted(word_list, key=lambda x: (-x[1], x[0]))
        c = 0
        for w in word_list:
            if w[1]:
                print("{}: {}".format(w[0], w[1]))
            else:
                c += 1
        if c == len(word_list):
            print("")
        return None

    url = REDDIT + "r/{}/hot/.json".format(subreddit)

    params = {
        'limit': 100,
        'after': after
    }

    r = get(url, headers=HEADERS, params=params, allow_redirects=False)

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
            title = post.get("title")
            lower = [s.lower() for s in title.split(' ')]

            for w in word_list:
                count = lower.count(w[0])
                w[1] += count

    except:
        return None

    count_words(subreddit, word_list, after)
