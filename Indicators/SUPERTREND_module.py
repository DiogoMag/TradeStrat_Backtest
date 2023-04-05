import yfinance as yf
import pandas_ta as ta
import pandas as pd
import seaborn as sns
import time

while True:
    # Request the ticker data for BTCUSDT
    ticker = yf.Ticker("BTC-USD")
    
    # Get the current price
    current_price = ticker.info['regularMarketPrice']
    
    # Print the current price
    print("BTCUSDT Price: ", current_price)
    
    # Wait for 5 seconds before repeating the loop
    time.sleep(5)
