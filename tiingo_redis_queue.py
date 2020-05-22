import os
from time import time

from redis import Redis
from rq import Queue
import ujson

from tiingo_get import get_eod_price as fn
from tiingo_logger import logger


def main():
    start = time()
    
    with open('Technology-2019-11-10.json', 'r') as r:
        stocks = ujson.load(r)
    
    q = Queue(connection=Redis('127.0.0.1', port=6379))
    for i, stock in enumerate(stocks, 1):
        q.enqueue(fn, stock, i)


if __name__ == '__main__':
    main()