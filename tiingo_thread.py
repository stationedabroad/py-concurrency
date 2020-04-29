import json
import threading
import time
from tiingo_get import get_eod_price as fn


if __name__ == '__main__':
    st = time.time()
    with open('Technology-2019-11-10.json', 'r') as r:
        stocks = json.load(r)
    
    jobs = []
    for i, ticker in enumerate(stocks):
        thread = threading.Thread(target=fn(ticker['symbol_code'], i))
        jobs.append(thread)

    for j in jobs:
        j.start()
    for j in jobs:
        j.join()                

    print('Threaded processing finished ...')
    elapsed = time.time() - st
    print(f'Threaded processing = {elapsed}')