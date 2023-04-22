import matplotlib.pyplot as plt
import mplfinance as mpf
from binance import Client
import pandas as pd
import os

os.system('cls')

test_api_key = os.environ.get('TEST_API')
test_api_secret = os.environ.get('TEST_SAPI')

client = Client(test_api_key, test_api_secret)

asset = 'BTCUSDT'

def get_minute_data(symbol, interval, lookback):
    frame = pd.DataFrame(client.get_historical_klines(symbol, interval, lookback + ' min ago UTC'))
    frame = frame.iloc[:,:6]
    frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume' ]
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame = frame.astype(float)
    return frame

df = get_minute_data(asset, '5m', '120m')
