from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class SeleniumDriver(object):
    
    # ブラウザーを起動
    def start_driver(self):
        options = Options()
        driver = webdriver.Chrome(options=options,executable_path="../chromedriver")
        return driver

    #ブラウザーの終了
    def quit_driver(self,driver):
        driver.quit()
