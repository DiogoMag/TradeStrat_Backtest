import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pandas as pd
import pandas_ta as ta
import yfinance as yf
import mplfinance as mpf
import datetime

class App:
    def __init__(self, master):
        self.master = master
        master.title("Data Fetcher")
        master.geometry("500x500")


        self.symbol_label = tk.Label(master, text="Symbol", font='bold')
        self.symbol_label.pack()
        self.tips_label = tk.Label(master, text="(  Forex: 'EURUSD=X',   Crypto: 'BTC-USD',   Stocks: 'MSFT'  )")
        self.tips_label.pack()
        self.tips_label = tk.Label(master, text="Separate multiples with ' , '")
        self.tips_label.pack()

        self.symbol_entry_var = tk.StringVar(value="EURUSD=X")
        self.symbol_entry = tk.Entry(master, textvariable=self.symbol_entry_var)
        self.symbol_entry.pack()

        self.period_label = tk.Label(master, text="Period", font='bold')
        self.period_label.pack()
        self.period_combobox = ttk.Combobox(master, values=['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'])
        self.period_combobox.current(0)
        self.period_combobox.pack()

        self.interval_label = tk.Label(master, text="Interval", font='bold')
        self.interval_label.pack()
        self.interval_combobox = ttk.Combobox(master, values=['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo'])
        self.interval_combobox.current(2)
        self.interval_combobox.pack()

        separator = ttk.Separator(root, orient='horizontal')
        separator.pack(fill='x', pady=10)

        self.ema20_var = tk.BooleanVar(value=False)
        self.ema50_var = tk.BooleanVar(value=False)
        self.ema200_var = tk.BooleanVar(value=False)

        self.ema20_checkbutton = tk.Checkbutton(master, text="EMA 20", variable=self.ema20_var)
        self.ema20_checkbutton.pack()

        self.ema50_checkbutton = tk.Checkbutton(master, text="EMA 50", variable=self.ema50_var)
        self.ema50_checkbutton.pack()

        self.ema200_checkbutton = tk.Checkbutton(master, text="EMA 200", variable=self.ema200_var)
        self.ema200_checkbutton.pack()
        separator = ttk.Separator(root, orient='horizontal')
        separator.pack(fill='x', pady=10)

        self.plot_button = tk.Button(master, text="Plot CSV", command=self.plot_csv)
        self.plot_button.pack()

        self.get_button = tk.Button(master, text="Get Symbol Data", command=self.get_data)
        self.get_button.pack()

        self.this_csv = None

    def identify_session(tempo_str):
        # convert tempo_str to datetime.time object
        try:
            tempo = datetime.datetime.strptime(tempo_str, '%H:%M:%S').time()
        except ValueError:
            tempo = datetime.datetime.strptime(tempo_str, '%H:%M').time()

        # define time ranges and corresponding session values
        time_ranges = [
            (datetime.time(hour=13), datetime.time(hour=22), 'NewYork'),
            (datetime.time(hour=7), datetime.time(hour=16), 'London'),
            (datetime.time(hour=0), datetime.time(hour=9), 'Tokyo'),
            (datetime.time(hour=0), datetime.time(hour=6), 'Sidney'),
        ]
        
        # initialize session to an empty string
        session = ""
        
        # check if the tempo is within any of the time ranges and concatenate session values if needed
        for start_time, end_time, session_val in time_ranges:
            if start_time <= tempo <= end_time:
                if session == "":
                    session = session_val
                else:
                    session += f",{session_val}"
        
        return session

    def plot_df_to_kline(self, df):

        mc = mpf.make_marketcolors(up='g', down='r')
        my_style = mpf.make_mpf_style(marketcolors=mc) 
                
        # Create addplot list for EMAs
        ### Single EMAs
        if self.ema20_var.get() == True and self.ema50_var.get() == False and self.ema200_var.get() == False :
            ema = mpf.make_addplot(df['EMA 20'], color='blue', width=0.7)
            mpf.plot(df, type='candle', ylabel='Price', figratio=(16,8), style=my_style, addplot=ema, show_nontrading=True)

        elif self.ema20_var.get() == False and self.ema50_var.get() == True and self.ema200_var.get() == False :
            ema = mpf.make_addplot(df['EMA 50'], color='green', width=0.7)
            mpf.plot(df, type='candle', ylabel='Price', figratio=(16,8), style=my_style, addplot=ema, show_nontrading=True)

        elif self.ema20_var.get() == False and self.ema50_var.get() == False and self.ema200_var.get() == True :
            ema = mpf.make_addplot(df['EMA 200'], color='orange', width=0.7)
            mpf.plot(df, type='candle', ylabel='Price', figratio=(16,8), style=my_style, addplot=ema, show_nontrading=True)
        
        ### 2 EMAs
        elif self.ema20_var.get() == True and self.ema50_var.get() == True and self.ema200_var.get() == False :
            ema1 = mpf.make_addplot(df['EMA 20'], color='blue', width=0.7)
            ema2 = mpf.make_addplot(df['EMA 50'], color='green', width=0.7)
            mpf.plot(df, type='candle', ylabel='Price', figratio=(16,8), style=my_style, addplot=[ema1, ema2] , show_nontrading=True)
        
        elif self.ema20_var.get() == True and self.ema50_var.get() == False and self.ema200_var.get() == True :
            ema1 = mpf.make_addplot(df['EMA 20'], color='blue', width=0.7)
            ema3 = mpf.make_addplot(df['EMA 200'], color='orange', width=0.7)
            mpf.plot(df, type='candle', ylabel='Price', figratio=(16,8), style=my_style, addplot=[ema1, ema3] , show_nontrading=True)
        
        elif self.ema20_var.get() == False and self.ema50_var.get() == True and self.ema200_var.get() == True :
            ema2 = mpf.make_addplot(df['EMA 50'], color='green', width=0.7)
            ema3 = mpf.make_addplot(df['EMA 200'], color='orange', width=0.7)
            mpf.plot(df, type='candle', ylabel='Price', figratio=(16,8), style=my_style, addplot=[ema2, ema3] , show_nontrading=True)
        
        ### All 3 EMAs
        elif self.ema20_var.get() == True and self.ema50_var.get() == True and self.ema200_var.get() == True :
            ema1 = mpf.make_addplot(df['EMA 20'], color='blue', width=0.7)
            ema2 = mpf.make_addplot(df['EMA 50'], color='green', width=0.7)
            ema3 = mpf.make_addplot(df['EMA 200'], color='orange', width=0.7)
            mpf.plot(df, type='candle', ylabel='Price', figratio=(16,8), style=my_style, addplot=[ema1, ema2, ema3] , show_nontrading=True)

        else:
            ema = None        
            mpf.plot(df, type='candle', ylabel='Price', figratio=(16,8), style=my_style, show_nontrading=True)
    
    def get_data(self):
        symbol = self.symbol_entry.get()
        X_period = self.period_combobox.get()
        X_interval = self.interval_combobox.get()

        data = yf.download(symbol, period=X_period, interval=X_interval)
        data = data.drop(['Volume', 'Adj Close'], axis=1)

        ## Add EMA 20 50 200
        data['EMA 20'] = ta.ema(data['Close'], length=20)
        data['EMA 50'] = ta.ema(data['Close'], length=50)
        data['EMA 200'] = ta.ema(data['Close'], length=200)

        self.this_csv = f'{symbol}_{X_interval}_{X_period}.csv'
        data.to_csv('calculatorLogs/' + self.this_csv)

    def plot_csv(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            df = pd.read_csv(file_path, index_col=0, parse_dates=True)
            self.plot_df_to_kline(df)


root = tk.Tk()
app = App(root)
root.mainloop()
