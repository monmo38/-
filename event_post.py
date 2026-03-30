import json
import os
import random
import urllib.parse
import urllib.request

ACCESS_TOKEN = os.environ["THREADS_ACCESS_TOKEN"]
USER_ID = os.environ["THREADS_USER_ID"]

BASE_IMAGE_URL = "https://monmo38.github.io/threads-assets/images"

EVENT_POSTS = [
    {
        "slug": "english_cave_ja",
        "image_url": f"{BASE_IMAGE_URL}/english_cave_ja.jpg",
        "text": "当店で開催しているイベントの紹介です！\n"
        "【世界の言語を使ってコミニュケーション！】\n\n"
        "海外のお客様もよく来られるボードゲームカフェ リトルケイブ新宿南口店です！\n\n"
        "不定期で開催している言語交換会\n"
        "“イングリッシュケイブ”\n\n"
        "外国語を勉強中の人達で集まって緩く始まるボドゲ会！\n"
        "ノリと勢いだけで何とかなっています！\n"
        "異文化コミュニケーションの練習にお使いください！\n\n"
        "日付が決まったらお伝えします！",
    },
    {
        "slug": "english_cave_en",
        "image_url": f"{BASE_IMAGE_URL}/english_cave_en.jpg",
        "text": "Here’s one of the events at Little Cave Shinjuku South Exit!\n\n"
        "English Cave is a casual board game event for language exchange.\n\n"
        "We often welcome international guests, making it a great chance to practice cross-cultural communication.\n\n"
        "We’ll share the date once it’s set.",
    },
    {
        "slug": "snap_shot_cave",
        "image_url": f"{BASE_IMAGE_URL}/snap_shot_cave.jpg",
        "text": "おそらくリトルケイブ新宿南口店だけでやっているチェキ的なサービス！\n"
        "【思い出をシールにして持ち帰ろう！】\n\n"
        "“Snap Shot Cave”\n\n"
        "SNSで当店を宣伝してくださったお客様のお好きな写真をシール化するサービスを開始いたしました！\n\n"
        "シールにする写真はご自身のスマホに元からあるものでもお店にあるカメラで今撮影したものでもOK！\n"
        "雰囲気のあるモノクロシールになります！\n\n"
        "手帳勢におススメのサービスです！\n"
        "是非挑戦してみてください！",
    },
    {
        "slug": "under30_cave",
        "image_url": f"{BASE_IMAGE_URL}/under30_cave.jpg",
        "text": "当店で開催している若者向けサービスデーのご案内！\n"
        "【アンダー３０ケイブ】\n\n"
        "入学前のお子様からシニア世代の方まで幅広くご利用頂いているボードゲームカフェ リトルケイブ新宿南口店です！\n\n"
        "当店は不定期で世代割が適用される日\n"
        "“アンダー３０ケイブ”と“オーバー３０ケイブ”があります！\n\n"
        "“アンダー３０ケイブ”は２９歳までのお客様ならワンドリンクが無料！\n"
        "学割とも併用できますので学生の方は是非この日を狙いましょう！\n\n"
        "日付が決まったらお伝えします！",
    },
    {
        "slug": "over30_cave",
        "image_url": f"{BASE_IMAGE_URL}/over30_cave.jpg",
        "text": "当店で開催している落ち着いた人向けサービスデーのご案内！\n"
        "【オーバー３０ケイブ】\n\n"
        "入学前のお子様からシニア世代の方まで幅広くご利用頂いているボードゲームカフェ リトルケイブ新宿南口店です！\n\n"
        "当店は不定期で世代割が適用される日\n"
        "“アンダー３０ケイブ”と“オーバー３０ケイブ”があります！\n\n"
        "“オーバー３０ケイブ”は３０歳からのお客様ならワンドリンクが無料！\n"
        "皆様のご来店をお待ちしております！\n\n"
        "日付が決まったらお伝えします！",
    },
    {
        "slug": "work_cafe_plan",
        "image_url": f"{BASE_IMAGE_URL}/work_cafe_plan.jpg",
        "text": "リトルケイブ新宿南口店で利用できる特殊料金プランのご紹介！\n"
        "【作業カフェプラン】\n\n"
        "平日、遊びさえしなければこのプラン！\n"
        "混雑時以外は何時間利用しても1600円+1D！\n\n"
        "お店の備品は資料として使い放題！\n"
        "お腹が空いたら料理の注文もしていただけます！\n\n"
        "よくある面倒な会員登録や時間ごとの注文の強制もなくのびのび利用頂けます！\n"
        "Wi-Fiと電源も完備！\n\n"
        "詳細\n"
        "https://studio-cave.com/littlecave/shinjuku/2025/01/23/%e3%83%9c%e3%83%89%e3%82%b2%e8%a3%bd%e4%bd%9c%e8%80%85%e5%bf%9c%e6%8f%b4%ef%bc%81%e3%80%90%e4%bd%9c%e6%a5%ad%e3%82%ab%e3%83%95%e3%82%A7%E3%83%97%E3%83%A9%E3%83%B3%E3%80%91%E7%99%BB%E5%A0%B4%EF%BC%81/",
    },
    {
        "slug": "murder_mystery_and_puzzle",
        "image_url": f"{BASE_IMAGE_URL}/murder_mystery_and_puzzle.jpg",
        "text": "当店で取り扱っているサービスのご案内！\n"
        "【当店でマダミスや謎解きの取り扱いがございます】\n\n"
        "ボードゲームカフェ リトルケイブ新宿南口店ではお店で買って遊べるマーダーミステリーや推理ゲームを取り揃えています！\n"
        "2人で出来る商品が特に多いです！\n\n"
        "持ち帰って遊ぶもよし、お店で遊んでもよし、用途に合わせてお楽しみください！\n\n"
        "※購入商品のみ。試遊用のサンプルはございません。",
    },
    {
        "slug": "lorcana_pack_rush",
        "image_url": f"{BASE_IMAGE_URL}/lorcana_pack_rush.png",
        "text": "リトルケイブ新宿南口店のイベント開催情報！\n"
        "【当店はロルカナ公認店です】\n\n"
        "ロルカナ\n"
        "ディズニー公式のTCG\n"
        "キャラクターたちが繰り広げる戦いを楽しめます。\n\n"
        "みんなでカードパックを買ってランダムなカードで戦う“パックラッシュ”も不定期で行っております！\n\n"
        "詳細\n"
        "https://tonamel.com/organization/r8Tav?game=disneylorcana\n\n"
        "※よく分からないけどやってみたい方はとにかくご来店ください！ご説明します！",
    },
    {
        "slug": "lorcana_store",
        "image_url": f"{BASE_IMAGE_URL}/lorcana_store.png",
        "text": "リトルケイブ新宿南口店はボドゲだけじゃない！\n"
        "【当店はロルカナ公認店です】\n\n"
        "“ロルカナ”\n"
        "ディズニー公式のTCG\n"
        "キャラクターたちが繰り広げる戦いを楽しめます。\n\n"
        "当店では関連商品が購入できる他、交流会や対戦会を開いております！\n\n"
        "詳細\n"
        "https://tonamel.com/organization/r8Tav?game=disneylorcana\n\n"
        "※よく分からないけどやってみたい方はとにかくご来店ください！ご説明します！",
    },
    {
        "slug": "student_discount",
        "image_url": f"{BASE_IMAGE_URL}/student_discount.jpg",
        "text": "リトルケイブ新宿南口店のお得な料金プラン！\n\n"
        "【学割サービス】\n\n"
        "平日だけ使えるリトルケイブの学割！\n\n"
        "通常利用より大幅にお安く出来ます！\n\n"
        "12-17もしくは17-23というタイムテーブルにしておりますが、それ以外の時間帯の利用の場合でもこちらで一番安くなるように調整・説明します！\n\n"
        "さらに９歳以下は全日利用料無料です！\n"
        "ご家族でご利用の方は必ずお伝えください！",
    },
    {
        "slug": "traditional_cave_ja",
        "image_url": f"{BASE_IMAGE_URL}/traditional_cave_ja.jpg",
        "text": "当店で開催している相席イベントをご紹介！\n"
        "【トランプやドミノなどの伝統ゲームを遊ぶ会】\n\n"
        "初心者にもおススメのボドゲカフェ リトルケイブ新宿南口店です！\n\n"
        "当店で不定期に開催される\n"
        "伝統的なゲームを遊ぶ会“トラディショナルケイブ”！\n\n"
        "主催の草場純様によるドミノやトランプなど歴史あるゲームを遊ぶ会です！\n"
        "今はもう後継者がいなくなってしまった地域で伝わっていた手遊びなども学べます！\n\n"
        "ルールを覚えて家族や友達とも遊びましょう！\n\n"
        "日付が決まったらお伝えします！\n"
        "※トランプの使用については原宿警察署に相談済みです。",
    },
    {
        "slug": "traditional_cave_en",
        "image_url": f"{BASE_IMAGE_URL}/traditional_cave_en.jpg",
        "text": "Here’s one of the events at Little Cave Shinjuku South Exit!\n\n"
        "Traditional Cave is a casual event where you can play classic games like cards and dominoes.\n\n"
        "Hosted by Jun Kusaba, it’s a chance to learn traditional games passed down over time.\n\n"
        "We’ll share the date once it’s decided.",
    },
    {
        "slug": "wednesday_meeting_r",
        "image_url": f"{BASE_IMAGE_URL}/wednesday_meeting_r.jpg",
        "text": "当店で開催している定期イベントをお知らせします！\n"
        "【水曜日の会R】\n\n"
        "仕事帰りにも寄りやすいボードゲームカフェ リトルケイブ新宿南口店です！\n\n"
        "毎月第一水曜日と第三水曜日は相席ボードゲーム会の“水曜日の会R”！\n\n"
        "国内で最初の頃に始まったオープン会の一つ！\n"
        "歴史あるオープン会がリトルケイブ新宿南口店に引き継がれました！\n"
        "まだ日本で販売していない海外のゲームや、今はもう入手困難な昔のレアゲーなど、普段は出来ないような名作に出会えます！",
    },
    {
        "slug": "good_morning_cave",
        "image_url": f"{BASE_IMAGE_URL}/good_morning_cave.jpg",
        "text": "リトルケイブ新宿南口店限定の特殊な料金プラン！\n"
        "【グッドモーニングケイブ】\n\n"
        "平日の朝から遊び尽くせる貸切プラン！\n\n"
        "20名で5時間利用したとしたら一人900円！\n"
        "つまり１ｈ/180円！\n\n"
        "しかも飲食物の持ち込みもOK！持ち込み料も頂きません！\n"
        "本当に利用料金だけでお遊び頂けます！\n\n"
        "イベンターの方におススメのプランとなっております！\n\n"
        "詳細\n"
        "https://studio-cave.com/littlecave/shinjuku/2025/01/28/%e6%9c%9d%e6%b4%bb%e3%81%ab%e3%82%aa%e3%82%B9%E3%82%B9%E3%83%A1%E3%81%AE%E5%88%A9%E7%94%A8%E3%83%97%E3%83%A9%E3%83%B3%EF%BC%81%E3%80%90%E3%82%B0%E3%83%83%E3%83%89%E3%83%A2%E3%83%BC%E3%83%8B%E3%83%B3/",
    },
    {
        "slug": "second_thursday_game_meeting",
        "image_url": f"{BASE_IMAGE_URL}/second_thursday_game_meeting.jpg",
        "text": "当店で開催している定期開催中の相席イベント紹介！\n"
        "【第二木曜ゲーム会】\n\n"
        "新宿駅出てすぐのボドゲカフェ リトルケイブ新宿南口店です！\n\n"
        "当店では毎月第二木曜日にお一人様同士集まってボードゲーム会をしております！\n"
        "もちろんお二人以上のグループでもご参加いただけます！\n\n"
        "普段できないゲームをみんなで遊ぶチャンス！\n"
        "お店のイベントが初めての人も大丈夫です！\n"
        "スタッフがまとめてサポートいたします！",
    },
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
    post_item = EVENT_POSTS[index]

    text = post_item["text"]
    image_url = post_item["image_url"]

    if not image_url:
        raise RuntimeError(f"Error: image_url missing for index {index}")

    create_url = f"https://graph.threads.net/v1.0/{USER_ID}/threads"
    create_data = {
        "media_type": "IMAGE",
        "image_url": image_url,
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
