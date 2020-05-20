"""
Load data
Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
As a result, store all comments in chronological order in JSON and dump it to a file.
"""

import requests
import argparse
import json

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Comments from subreddit')
    parser.add_argument('subreddit', action="store", help="subreddit name")
    args = parser.parse_args()
    response = requests.get("https://api.pushshift.io/reddit/comment/search/?subreddit=" + args.subreddit)
    comments = sorted(response.json()["data"], key=lambda k: k['created_utc'])
    with open(f"{args.subreddit}_comments.json", "w", encoding=response.encoding) as f:
        json.dump(comments, f)
