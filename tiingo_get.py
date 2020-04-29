import requests
import os


def get_eod_price(stock, caller_id):

    header = {
        'Content-Type': 'application/json'
    }    

    token = os.getenv("TIINGO_TK")
    url = "https://api.tiingo.com/tiingo/daily/{}/prices?token={}"
    

    try:
        url = url.format(stock, token)
        content = requests.get(url, headers=header)
        status = content.status_code
    except Exception as e:
        status = None
        print(f"exception during API call - {e}")
    
    print(f'Call - {caller_id} completed with status - {status}')