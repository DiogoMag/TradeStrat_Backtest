import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
from binance import Client
import pandas as pd
import os

test_api_key = os.environ.get('test_api_key')
test_api_secret = os.environ.get('test_api_secret')

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

fig, ax = plt.subplots()
ax.set_xlabel('Time')
ax.set_ylabel('Price')
ax.set_title(asset)

line, = ax.plot([], [])

def animate(i):
    data = get_minute_data(asset, '1m', '120m')
    line.set_data(data.index, data.Close)
    ax.relim()
    ax.autoscale_view()
    fig.autofmt_xdate()

canvas_width = 600
canvas_height = 400

root = tk.Tk()
root.title("Live Plot")

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

fig_canvas = FigureCanvasTkAgg(fig, master=canvas)
fig_canvas.get_tk_widget().pack()

ani = FuncAnimation(fig, animate, interval=1000, save_count=len(df), cache_frame_data=False)

exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(side="bottom")

root.mainloop()
