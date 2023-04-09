import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from binance import Client
import pandas as pd
import os


test_api_key = os.environ.get('test_api_key')
test_api_secret = os.environ.get('test_api_secret')

plt.style.use('ggplot')

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

df = get_minute_data(asset, '1m', '120m')

def animate(i):
    data = get_minute_data(asset, '1m', '120m')
    plt.cla()
    plt.plot(data.index, data.Close, color='red', linewidth=3)
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title(asset)
    plt.gcf().autofmt_xdate()
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, 10000)

plt.tight_layout()
plt.show()