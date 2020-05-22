import ujson
import logging
from multiprocessing.pool import Pool
from time import time

from tiingo_get import _get_eod_price as fn

logging.basicConfig(                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        level=logging.INFO,
        filename='pylog.log',
        format='%(asctime)s: %(process)d - %(levelname)s - %(message)s',
        datefmt='%d-%b-%yy %H:%M:%S'
)

logger = logging.getLogger(__name__)

def get_stocks(stock_json):
    return [stock['symbol_code'] for stock in stock_json]
    

def main():
    start = time()
    
    with open('Technology-2019-11-10.json', 'r') as r:
        stocks = get_stocks(ujson.load(r))

    with Pool(12) as p:
        p.map(fn, stocks)

    elapsed = time() - start
    logger.info(f'Total run time {elapsed}')
    print(f'Total time: {elapsed}')


if __name__ == '__main__':
    main()