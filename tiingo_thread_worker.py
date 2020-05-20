import ujson
import logging
from queue import Queue
from threading import Thread
from time import time

from tiingo_get import get_eod_price as fn

logging.basicConfig(                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        level=logging.INFO,
        filename='pylog.log',
        format='%(asctime)s: %(process)d - %(levelname)s - %(message)s',
        datefmt='%d-%b-%yy %H:%M:%S'
)

logger = logging.getLogger(__name__)

class TiingoApi(Thread):

    def __init__(self, queue, logger, daemon):
        Thread.__init__(self, daemon=daemon)
        self.queue = queue
        self.logger = logger

    def run(self):
        while True:
            ticker, id = self.queue.get()
            self.logger.info(f'Thread entered for: {ticker} with id: {id}')
            try:
                fn(ticker, id)
            except Exception as e:
                self.logger.error(f'API error for ticker: {ticker}')
            finally:
                self.queue.task_done()
                self.logger.info(f'Processing complete for: {ticker} with id: {id}')


def main():
    start = time()

    queue = Queue()
    # set cores
    for _ in range(4):
        worker = TiingoApi(queue, logger, daemon=True)
        worker.start()

    with open('Technology-2019-11-10.json', 'r') as r:
        stocks = ujson.load(r)

    for id, stock in enumerate(stocks, 1):
        logger.info(f'Queueing {stock} for api call ...')
        queue.put((stock, id))
    queue.join()
    elapsed = time() - start
    logger.info(f'Total run time {elapsed}')
    print(f'Total time: {elapsed}')


if __name__ == '__main__':
    main()