import time
from workers.WikiWorkers import WikiWorker
from workers.YahooFinanceWorkers import YahooFinanceWorker


def main():
    scraper_start_time = time.time()

    wiki_worker = WikiWorker()
    current_workers = []
    for symbol in wiki_worker.get_sp_500_companies():

        yahoo_finance_worker = YahooFinanceWorker(symbol=symbol)
        current_workers.append(yahoo_finance_worker)

    for i in range(len(current_workers)):
        current_workers[i].join()

    print(f"Extracting time took: {round(time.time() - scraper_start_time, 1)}")


if __name__ == '__main__':
    main()
