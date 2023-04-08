
### This is super de-syncd but it works


import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.ticker import ScalarFormatter
from binance.client import Client

api_key = 'your_api_key'
api_secret = 'your_api_secret'
client = Client(api_key, api_secret, testnet=True)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

interval_seconds = 60
minutes_to_fetch = 1
num_intervals = (1 * minutes_to_fetch) // interval_seconds
start_time = int((datetime.datetime.now() - datetime.timedelta(minutes=minutes_to_fetch)).timestamp() * 1000)

def animate(i):
    global start_time
    klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1MINUTE, start_str=start_time)
    if len(klines) > 0:
        klines = [float(x[4]) for x in klines]
        start_time += interval_seconds * 1000
        xs.append(start_time)
        ys.append(klines[-1])
        ax.clear()
        ax.plot(xs, ys)
        plt.xticks(rotation=45)
        ax.yaxis.set_major_formatter(ScalarFormatter(useOffset=False))

ani = animation.FuncAnimation(fig, animate, interval=5000, cache_frame_data=False)
plt.show()
