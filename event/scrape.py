

def event_scrape(event,dic,soup):
    # イベントのタイトル
    dic["title"] = event.get_title(soup)
    # ライブの種類
    dic["live_type"] = event.get_live_type(soup)
    # イベント開始時間
    attribute={"data-field":"start_date"}
    dic["start_time"]=event.get_event_time(soup,attribute)
    # イベント終了時間
    attribute={"data-field":"end_date"}
    dic["end_time"]=event.get_event_time(soup,attribute)
    # イベント報酬のカード
    dic["event_card_list"] =event.get_event_card(soup)
    # 配布楽曲
    dic["event_music"] = event.get_event_music(soup)
    # 登場キャラリスト(キャラ名のみ)
    dic["chara_list"] = event.get_event_chara(soup)
    #イベントロゴ
    dic["event_image"]=event.get_event_img(soup)
    return dic


def gacha_scrape(gacha,dic,soup):
    #ガチャ名前
    dic["gacha_title"]=gacha.get_gacha_title(soup)
    #ガチャの種類
    dic["gacha_type"]=gacha.get_gacha_type(soup)
    #ガチャの画像
    dic["gacha_image"] = gacha.get_gacha_image(soup)
    # # ガチャ開始
    dic["gacha_start"]=gacha.get_gacha_time(soup,"start")
    # # ガチャ終了(3)
    dic["gacha_end"]=gacha.get_gacha_time(soup,"end")
    # # ガチャ新規のカード(4)
    dic["gacha_card_list"]=gacha.get_gacha_chara(soup)
    return dic