from binance import Client
import pandas as pd
import os


## Clear screen
os.system('cls')

## Connect to binance client
test_api_key = os.environ.get('TEST_API')
test_api_secret = os.environ.get('TEST_SAPI')
client = Client(test_api_key, test_api_secret, testnet=True)

## Define asset for analysis
asset = 'BTC'

def get_account_balance(ticker):
    print('1')


get_account_balance('all')