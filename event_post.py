import json
import os
import random
import urllib.parse
import urllib.request

ACCESS_TOKEN = os.environ["THREADS_ACCESS_TOKEN"]
USER_ID = os.environ["THREADS_USER_ID"]

EVENT_POSTS = [
    "て\nす",
    "て\nと",
    "ｔ\nｔ",
]

def post(url, data):
    req = urllib.request.Request(
        url,
        data=urllib.parse.urlencode(data).encode("utf-8"),
        method="POST",
    )
    with urllib.request.urlopen(req) as res:
        return json.loads(res.read().decode("utf-8"))

def main():
    text = random.choice(EVENT_POSTS)

    create_url = f"https://graph.threads.net/v1.0/{USER_ID}/threads"
    create_data = {
        "media_type": "TEXT",
        "text": text,
        "access_token": ACCESS_TOKEN,
    }
    created = post(create_url, create_data)
    creation_id = created["id"]

    publish_url = f"https://graph.threads.net/v1.0/{USER_ID}/threads_publish"
    publish_data = {
        "creation_id": creation_id,
        "access_token": ACCESS_TOKEN,
    }
    published = post(publish_url, publish_data)
    print(published)

if __name__ == "__main__":
    main()
