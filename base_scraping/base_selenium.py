class BaseSelenium(object):

    def find_elements(self,driver,xpath):
        elements = driver.find_elements_by_xpath(xpath)
        return elements

    def execute_script(self,driver,script):
        driver.execute_script(script)
    
    def get_pages_html(self,driver):
        html = driver.page_source.encode('utf-8')
        return html

    def move_page(self,driver,url):
        driver.get(url)
        return driver

    def click_element(self,element):
        element.click()

    