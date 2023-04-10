import matplotlib.pyplot as plt
from binance import Client
import pandas as pd
import os

os.system('cls')

test_api_key = os.environ.get('TEST_API')
test_api_secret = os.environ.get('TEST_SAPI')

client = Client(test_api_key, test_api_secret, testnet=True)

asset = 'BTCUSDT'

def get_minute_data(symbol, interval, lookback):
    frame = pd.DataFrame(client.get_historical_klines(symbol, interval, lookback + ' min ago UTC'))
    frame = frame.iloc[:,:6]
    frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume' ]
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame = frame.astype(float)
    return frame

df = get_minute_data(asset, '1m', '120m')

## PLOTING
fig, ax = plt.subplots()

ax.plot(df.index, df['Open'], color='green', label='Open')
ax.plot(df.index, df['High'], color='blue', label='High')
ax.plot(df.index, df['Low'], color='red', label='Low')
ax.plot(df.index, df['Close'], color='black', label='Close')

ax.legend()

plt.title(asset + ' 1 Minute Klines')
plt.xlabel('Time')
plt.ylabel('Price')

plt.show()