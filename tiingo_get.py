import os
import requests
from time import time

from tiingo_logger import logger


def get_eod_price(stock, caller_id):

    header = {
        'Content-Type': 'application/json'
    }    

    token = os.getenv("TIINGO_TK")
    url = "https://api.tiingo.com/tiingo/daily/{ticker}/prices?token={token}"
    

    try:
        url = url.format(ticker=stock, token=token)
        st = time()
        content = requests.get(url, headers=header)
        status = content.status_code
        logger.info(f'Tiingo APi call for {stock} completed in: {time() - st}')
    except Exception as e:
        status = None
        print(f"exception during API call - {e}")
        logger.error(f"Exception during SPI call for: {stock}, error: {e}")
        raise Exception(f'API error {url}')
    
    print(f'Call - {caller_id} completed for ticker: {stock} with status: {status}')