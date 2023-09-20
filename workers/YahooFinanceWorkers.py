import random
import threading
import time

from bs4 import BeautifulSoup
import requests
from lxml import html


class YahooFinanceWorker(threading.Thread):
    def __init__(self, symbol, **kwargs):
        super(YahooFinanceWorker, self).__init__(**kwargs)
        self._symbol = symbol
        base_url = 'https://finance.yahoo.com/quote/'
        self._url = f'{base_url}{self._symbol}'
        self.start()

    def run(self):
        time.sleep(30 * random.random())
        r = requests.get(self._url)
        if r.status_code != 200:
            return
        page_contents = html.fromstring(r.text)
        print(page_contents)
        price = page_contents.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]')
        print(price)
        final_price = float(price[0].text)
        print(final_price)
