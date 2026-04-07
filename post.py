import json
import os
import random
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

ACCESS_TOKEN = os.environ["THREADS_ACCESS_TOKEN"]
USER_ID = os.environ["THREADS_USER_ID"]

OPENING_POSTS = [
    "新宿駅最寄りのボードゲームカフェ\n"
    "リトルケイブ新宿南口店\n"
    "現在営業中です！\n\n"
    "23時CLOSE！\n"
    "※21:30 Food L.o ノーゲスで早締め\n\n"
    "終電ギリギリまで遊べる！\n"
    "カラオケやダーツに飽きたらボドゲカフェをご利用ください！\n\n"
    "当店は長く利用するほどお得となっております！\n"
    "是非ご利用ください！\n\n"
    "☎03-6300-6088",

    "新宿駅最寄りのボドゲカフェ\n"
    "リトルケイブ新宿南口店\n"
    "本日もOPENしています！\n\n"
    "23時まで営業！\n"
    "※21:30 Food L.o ノーゲスで早締め\n\n"
    "当店はほぼ毎日一組以上ボドゲ未経験の方が遊びに来ます！\n"
    "ですので、ボードゲームを全く知らない方でも大丈夫！手厚く歓迎いたします！\n\n"
    "是非ご利用ください！\n\n"
    "☎03-6300-6088",

    "新宿駅最寄りのボードゲームカフェ\n"
    "リトルケイブ新宿南口店OPENしています！\n\n"
    "23時まで営業！\n"
    "※21:30 Food L.o ノーゲスで早締め\n\n"
    "当店は人生初ボドゲカフェにおススメ！\n"
    "スタッフが店内の利用方法からゲームのルールまで全て説明いたします！\n"
    "予習は一切必要無し！お気軽にお越しください！\n\n"
    "☎03-6300-6088",

    "新宿駅最寄りのボードゲームカフェ\n"
    "リトルケイブ新宿南口店です！\n"
    "只今営業中です！\n\n"
    "23時閉店！\n"
    "※21:30 Food L.o ノーゲスで早締め\n\n"
    "学校や仕事終わり、約束前の空いた時間やデートの休憩にもご利用ください！\n"
    "実はご家族でご利用する方も多いんですよ！\n\n"
    "今週もよろしくお願いいたします！\n\n"
    "☎03-6300-6088",

    "新宿駅最寄りのボドゲカフェ\n"
    "リトルケイブ新宿南口店です！\n"
    "今日も営業中です！\n\n"
    "23時までOPEN！\n"
    "※21:30 Food L.o ノーゲスで早締め\n\n"
    "お食事だけや作業カフェとしてのご利用も頂けます！\n"
    "ボードゲームをやったこと無い人も大歓迎です！スタッフが全てご説明いたします！\n\n"
    "☎03-6300-6088",
]

INDEX_STATE_FILE = "opening_last_index.txt"
DATE_STATE_FILE = "opening_last_date.txt"

JST = timezone(timedelta(hours=9))


def post(url, data):
    req = urllib.request.Request(
        url,
        data=urllib.parse.urlencode(data).encode("utf-8"),
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as res:
            body = res.read().decode("utf-8")
            print("API response:", body)
            return json.loads(body)
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8", errors="replace")
        print("HTTPError status:", e.code)
        print("HTTPError body:", error_body)
        raise


def load_last_index():
    try:
        with open(INDEX_STATE_FILE, "r", encoding="utf-8") as f:
            return int(f.read().strip())
    except Exception:
        return None


def save_last_index(index):
    with open(INDEX_STATE_FILE, "w", encoding="utf-8") as f:
        f.write(str(index))


def load_last_date():
    try:
        with open(DATE_STATE_FILE, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception:
        return None


def save_last_date(date_str):
    with open(DATE_STATE_FILE, "w", encoding="utf-8") as f:
        f.write(date_str)


def choose_index(count, last_index):
    choices = list(range(count))
    if last_index is not None and count > 1 and last_index in choices:
        choices.remove(last_index)
    return random.choice(choices)


def today_jst():
    return datetime.now(JST).strftime("%Y-%m-%d")


def already_posted_today():
    return load_last_date() == today_jst()


def main():
    if already_posted_today():
        print("Already posted today in JST. Skipping.")
        return

    last_index = load_last_index()
    index = choose_index(len(OPENING_POSTS), last_index)
    text = OPENING_POSTS[index]

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
    save_last_date(today_jst())


if __name__ == "__main__":
    main()
