from binance import Client
import pandas as pd
import os


test_api_key = os.environ.get('TEST_API')
test_api_secret = os.environ.get('TEST_SAPI')

client = Client(test_api_key, test_api_secret, testnet=True)

asset = 'BTCUSDT'

print(test_api_key)
print(test_api_secret)

print(client.get_account())