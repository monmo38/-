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

STATE_FILE = "event_last_index.txt"

def post(url, data):
    req = urllib.request.Request(
        url,
        data=urllib.parse.urlencode(data).encode("utf-8"),
        method="POST",
    )
    with urllib.request.urlopen(req) as res:
        return json.loads(res.read().decode("utf-8"))

def load_last_index():
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            return int(f.read().strip())
    except:
        return None

def save_last_index(index):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        f.write(str(index))

def choose_index(count, last_index):
    choices = list(range(count))
    if last_index is not None and count > 1 and last_index in choices:
        choices.remove(last_index)
    return random.choice(choices)

def main():
    last_index = load_last_index()
    index = choose_index(len(EVENT_POSTS), last_index)
    text = EVENT_POSTS[index]

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

    save_last_index(index)

if __name__ == "__main__":
    main()
