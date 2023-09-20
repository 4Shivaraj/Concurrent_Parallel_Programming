import requests
from bs4 import BeautifulSoup


class WikiWorker:
    def __init__(self):
        self._url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

    @staticmethod
    def _extract_company_symbols(page_html):
        soup = BeautifulSoup(page_html, 'lxml')
        table = soup.find(id='constituents')
        print(table)
        table_rows = table.find_all('tr')
        for row in table_rows[1:]:
            symbol = row.find('td').text.split('\n')
            print(symbol)
            yield symbol

    def get_sp_500_companies(self):
        response = requests.get(self._url)
        if response.status_code != 200:
            print("Couldn't get entries")
            return []
        yield from self._extract_company_symbols(response.text)


if __name__ == '__main__':
    wiki_worker = WikiWorker()
    for symbol in wiki_worker.get_sp_500_companies():
        print(symbol)

