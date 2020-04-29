import requests
import os


def get_eod_price(stock, caller_id):

    header = {
        'Content-Type': 'application/json'
    }    

    token = os.getenv("TIINGO_TK")
    url = "https://api.tiingo.com/tiingo/daily/{ticker}/prices?token={token}"
    

    try:
        url = url.format(ticker=stock, token=token)
        content = requests.get(url, headers=header)
        status = content.status_code
    except Exception as e:
        status = None
        print(f"exception during API call - {e}")
    
    print(f'Call - {caller_id} completed for ticker: {stock} with status: {status}')