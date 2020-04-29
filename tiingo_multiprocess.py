import json
import multiprocessing
import time
from tiingo_get import get_eod_price as fn


if __name__ == '__main__':
    st = time.time()
    with open('Technology-2019-11-10.json', 'r') as r:
        stocks = json.load(r)
    
    jobs = []
    for i, ticker in enumerate(stocks):
        proc = multiprocessing.Process(target=fn, agrs=(ticker['symbol_code'], i))
        jobs.append(proc)

    for j in jobs:
        j.start()
    for j in jobs:
        j.join()                

    print('Multi-Process processing finished ...')
    elapsed = time.time() - st
    print(f'Multi-Process processing = {elapsed}')