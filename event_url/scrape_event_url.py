import sys
sys.path.append('../')
from base_scraping.selenium_driver import SeleniumDriver
from base_scraping.beautifulsoup_driver import BeautifulsoupDriver

from event_url.url_scraping import UrlScraping

def scrape_event_url():
    s_driver = SeleniumDriver()
    url_scraping=UrlScraping()
    bs_driver=BeautifulsoupDriver()
    #ドライバーの起動
    url="https://bandori.party/events/"
    driver=s_driver.start_driver()
    driver=url_scraping.move_page(driver,url)
    # 画面を最下層までスクロールする(10回のスクロール)
    url_scraping.scroll_to_the_bottom(driver,10)
    #bs4起動、urlを取得する
    html = url_scraping.get_pages_html(driver)
    soup = bs_driver.start_driver(html)
    urls=url_scraping.get_all_url(soup)
    print((str(len(urls)))+"個のurlを取得しました")
    #urlを書き込む
    path="data/event_url.txt"
    url_scraping.write_url_to_txt_file(path,urls)
    #終了処理
    s_driver.quit_driver(driver)


if __name__ == '__main__':
    scrape_event_url()

