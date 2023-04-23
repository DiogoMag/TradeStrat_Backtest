import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Set the ticker symbol and interval
symbol = "EURUSD=X"
period = '1day'
interval = "15m"


# Get the data from Yahoo Finance
df = yf.download(symbol, period=period, interval=interval)

# Remove the 'Volume' + 'Adj Close' column from the DataFrame
df= df.drop(['Volume', 'Adj Close'], axis=1)


