import re
import json

class EventScraping():

    def read_event_url_txt(self,path):
        with open(path,"r") as f:
            lines = f.readlines()
        return [line.rstrip() for line in lines]

    # イベントのタイトル
    def get_title(self,soup):
        span = soup.find('span',{'class':'verbose-name'})
        title = span.parent.parent.find_all('td')[1].get_text()
        return title.splitlines()[-3].replace("\t","")

    # ライブの種類
    def get_live_type(self,soup):
        tr = soup.find('tr',{"data-field":"type"})
        return tr.find_all("td")[1].get_text().replace("\n","").replace("\t","").replace("  ","")

    # イベント時間
    def get_event_time(self,soup,attribute):
        tr = soup.find('tr',attribute)
        text_lines = tr.find_all("td")[1].find_all("span")[0].get_text()
        text_list = text_lines.split()
        return text_list[0]+text_list[1]

    #イベント報酬のカード
    def get_event_card(self,soup):
        divs = soup.find_all("div",{"class":"images"})[1].find_all("a")
        return [div.find("img").get("alt") for div in divs] 

    #配布楽曲
    def get_event_music(self,soup):
        tr=soup.find('tr',{"data-field":re.compile("song")})
        if tr is not None:
            return tr.find("th").find("small").get_text()
        else:
            return "楽曲なし"

    #登場キャラリスト
    def get_event_chara(self,soup):
        atags = soup.find_all("div",{"class":"images"})[0].find_all("a")
        return [atag.get("data-ajax-title") for atag in atags]

    #イベントロゴのurl
    def get_event_img(self,soup):
        img=soup.find("img",{"class":"event-image"}).get("src")
        image = "https:" + img
        return image

    def write_event_to_json(self,path,dic):
        with open(path, 'w') as f:
            json.dump(dic, f, ensure_ascii=False,indent=14)
    