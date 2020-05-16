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

    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            ticker, id = self.queue.get()
            try:
                fn(ticker, id)
            finally:
                self.queue.done()


def main():
    start = time()

    queue = Queue()
    # set cores
    for x in range(4):
        worker = TiingoApi(queue)
        worker.daemon = True
        worker.start()

    with open('Technology-2019-11-10.json', 'r') as r:
        stocks = ujson.load(r)

    for id, stock in enumerate(stocks, 1):
        logger.info(f'Queueing {stock} for api call ...')
        queue.put((stock, id))
    queue.join()
    elapsed = time() - start
    logger.info(f'Total run time {elapsed}')
    print(f'Total time: {elapsed}'')


if __name__ == '__main__':
    main()