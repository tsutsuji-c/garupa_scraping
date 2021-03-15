from bs4 import BeautifulSoup
import lxml

class BeautifulsoupDriver(object):

    def start_driver(self,html):
        soup = BeautifulSoup(html, 'lxml')
        return soup