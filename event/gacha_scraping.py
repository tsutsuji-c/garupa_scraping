import time
import sys
sys.path.append('../')
from base_scraping.base_selenium import BaseSelenium




class GachaScraping(BaseSelenium):

    #gachaのモーダルをクリックで表示する
    def display_gacha_modal(self,driver,xpath):
        gacha_modal=self.find_elements(driver,xpath)
        element=gacha_modal[0]
        self.click_element(element)
        time.sleep(3)

    #ガチャの名前
    def get_gacha_title(self,soup):
        tr=soup.find("tr",{"data-field":"name"})
        td=tr.find_all("td")[1].text
        gacha_title=td.split()
        return gacha_title[0]+gacha_title[1]

    #ガチャの種類
    def get_gacha_type(self,soup):
        tr=soup.find("tr",{"data-field":'limited'})
        td=tr.find_all("td")[1].text
        gacha_type=td.split()
        return gacha_type

    #ガチャの画像
    def get_gacha_image(self,soup):
        tr=soup.find("tr",{"data-field":'image'})
        td=tr.find_all("td")[1]
        if td.find("a") is not None:
            gacha_image=td.find("a")["href"]
            return "htpps//"+gacha_image
        else:
            return "なし"

    #ガチャの時間
    def get_gacha_time(self,soup,timing):
        timing = timing +'_date'
        attribute={"data-field":timing}
        tr=soup.find("tr",attribute)
        gacha_time=tr.find("span",{"class":'datetime'}).text
        return gacha_time

    def get_gacha_chara(self,soup):
        # # ガチャ新規のカード(4)
        a_tags = soup.find_all("div",{"class":"images"})[0].find_all("a")
        gacha_card_list=[a_tag.find("img").get("alt") for a_tag in a_tags]
        return gacha_card_list