import time
from workers.WikiWorkers import WikiWorker
from workers.YahooFinanceWorkers import YahooFinanceScheduler
from multiprocessing import Queue


def main():
    symbol_queue = Queue()
    scraper_start_time = time.time()

    wiki_worker = WikiWorker()
    yahoo_finance_price_scheduler_threads = []
    yahoo_finance_price_scheduler = YahooFinanceScheduler(input_queue=symbol_queue)
    yahoo_finance_price_scheduler_threads.append(yahoo_finance_price_scheduler)
    for symbol in wiki_worker.get_sp_500_companies():
        symbol_queue.put(symbol)

    for i in range(len(yahoo_finance_price_scheduler_threads)):
        symbol_queue.put('DONE')

    for i in range(len(yahoo_finance_price_scheduler_threads)):
        yahoo_finance_price_scheduler_threads[i].join()

    print(f"Extracting time took: {round(time.time() - scraper_start_time, 1)}")


if __name__ == '__main__':
    main()
