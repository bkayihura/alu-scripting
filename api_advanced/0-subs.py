#!/usr/bin/python3
"""Queries the Reddit API for the subscriber count of a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers, or 0 if the subreddit is invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0 (by /u/bkayihura)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get("data", {}).get("subscribers", 0)
