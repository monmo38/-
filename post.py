import json
import os
import random
import urllib.parse
import urllib.request

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

def post(url, data):
    req = urllib.request.Request(
        url,
        data=urllib.parse.urlencode(data).encode("utf-8"),
        method="POST",
    )
    with urllib.request.urlopen(req) as res:
        return json.loads(res.read().decode("utf-8"))

def main():
    text = random.choice(OPENING_POSTS)

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
