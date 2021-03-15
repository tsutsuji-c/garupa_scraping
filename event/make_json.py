import time

from base_scraping.selenium_driver import SeleniumDriver
from base_scraping.base_selenium import BaseSelenium
from base_scraping.beautifulsoup_driver import BeautifulsoupDriver

from event.event_scraping import EventScraping
from event.gacha_scraping import GachaScraping
from event.scrape import event_scrape,gacha_scrape



def make_event_json():
    
    #データをjsonファイルに書き込む

    s_driver = SeleniumDriver()
    b_driver = BeautifulsoupDriver()
    base_selenium = BaseSelenium()
    event=EventScraping()
    gacha=GachaScraping()

    dic={}
    path ="data/event_url.txt"
    target_urls = event.read_event_url_txt(path)
    # target_url = target_urls[0:2]#テスト
    target_url = target_urls
    #ドライバーの起動
    driver=s_driver.start_driver()

    #必要な情報をスクレイピングして辞書で返す
    #eventページを遷移する
    for i,url in enumerate(target_url):
        e_num =f"event_{str(i+1)}"
        dic[e_num]={}
        dic[e_num]["event"]={}
        dic[e_num]["gacha"]={}

        base_selenium.move_page(driver,url)
        #gachaのモーダルをクリックで表示する
        xpath="//tr[contains(@data-field,'gacha')]/child::td[2]/child::a[1]"
        gacha.display_gacha_modal(driver,xpath)

        #beautifulsoup使用
        html = base_selenium.get_pages_html(driver)
        #event情報をスクレイピング
        soup = b_driver.start_driver(html)
        dic[e_num]["event"]=event_scrape(event,dic[e_num]["event"],soup)
        #gacha情報をスクレイピング
        gacha_soup=soup.find("div",{"id":'ajaxModal'})
        dic[e_num]["gacha"]=gacha_scrape(gacha,dic[e_num]["gacha"],gacha_soup)
        time.sleep(2)
    print(dic)
    path='data/event.json'
    event.write_event_to_json(path,dic)
    s_driver.quit_driver(driver)

    

if __name__ == '__main__':
    make_json()