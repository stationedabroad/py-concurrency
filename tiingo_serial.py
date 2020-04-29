from tiingo_get import get_eod_price as fn
import json
import time

if __name__ == '__main__':
    st = time.time()
    with open('Technology-2019-11-10.json', 'r') as r:
        stocks = json.load(r)
    
    for i, ticker in enumerate(stocks):
        fn(ticker['symbol_code'], i)

    print('Serial processing finished ...')
    elapsed = time.time() - st
    print(f'serial processing = {elapsed}')