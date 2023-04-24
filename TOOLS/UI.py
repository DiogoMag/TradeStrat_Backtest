import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pandas as pd
import yfinance as yf
import mplfinance as mpf
import os

class App:
    def __init__(self, master):
        self.master = master
        master.title("Data Fetcher")
        master.geometry("400x300")

        self.symbol_label = tk.Label(master, text="Symbol")
        self.symbol_label.pack()
        self.symbol_entry = tk.Entry(master)
        self.symbol_entry.pack()

        self.period_label = tk.Label(master, text="Period")
        self.period_label.pack()
        self.period_combobox = ttk.Combobox(master, values=["1d", "5d", "1mo", "1y", "5y", "ytd", "max"])
        self.period_combobox.pack()

        self.interval_label = tk.Label(master, text="Interval")
        self.interval_label.pack()
        self.interval_combobox = ttk.Combobox(master, values=["1m", "5m", "15m", "30m", "60m", "1h", "1d", "1mo"])
        self.interval_combobox.pack()

        self.plot_button = tk.Button(master, text="Plot CSV", command=self.plot_csv)
        self.plot_button.pack()

        self.get_button = tk.Button(master, text="Get Symbol Data", command=self.get_data)
        self.get_button.pack()

        self.this_csv = None

        master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def plot_df_to_kline(self, df):
        mc = mpf.make_marketcolors(up='g', down='r')
        my_style = mpf.make_mpf_style(marketcolors=mc)
        mpf.plot(df, type='candle', ylabel='Price', figratio=(16,8), style=my_style)

    def get_data(self):
        symbol = self.symbol_entry.get()
        X_period = self.period_combobox.get()
        X_interval = self.interval_combobox.get()

        data = yf.download(symbol, period=X_period, interval=X_interval)
        data = data.drop(['Volume', 'Adj Close'], axis=1)
        self.this_csv = f'{symbol}_{X_interval}_{X_period}.csv'
        data.to_csv(self.this_csv)

    def on_closing(self):
        if self.this_csv is not None and os.path.exists(self.this_csv):
            os.remove(self.this_csv)
        self.master.destroy()

    def plot_csv(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            df = pd.read_csv(file_path, index_col=0, parse_dates=True)
            self.plot_df_to_kline(df)


root = tk.Tk()
app = App(root)
root.mainloop()
