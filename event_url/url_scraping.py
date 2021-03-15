import time
import re
import sys
sys.path.append('../')
from base_scraping.base_selenium import BaseSelenium

class UrlScraping(BaseSelenium):

    def scroll_to_the_bottom(self,driver,num):
        counter=0
        while counter < num:
            self.execute_script(driver,"window.scrollTo(0, document.body.scrollHeight);")
            counter += 1
            time.sleep(4)
        print("スクロール完了")
    
    def get_all_url(self,soup):
        a_tags=soup.find_all("a",href = re.compile('/event/(.+)'))
        return ["https://bandori.party"+str(a_tag.get("href")) for a_tag in a_tags]

    def find_all_elements(self,soup,tag,a):
        elements=soup.find_all(tag,a)
        return elements

    def write_url_to_txt_file(self,path,urls):
        with open(path,"w") as f:
            for url in urls:
                f.write(url +"\n")