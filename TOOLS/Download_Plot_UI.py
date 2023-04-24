import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import pandas_ta as ta

# Set Variables
symbol= 'EURUSD'
sta_date= '2023-04-01'
end_date= '2023-04-23'
X_interval= '15m'
X_period= '5d'

# download data for EUR/USD for the specified dates
data = yf.download(f'{symbol}=X', period=X_period, interval=X_interval)
data = data.drop(['Volume', 'Adj Close'], axis=1)

# Add SMA
data['SMA 10'] = data.ta.sma(10)
data['SMA 50'] = data.ta.sma(50)
data['SMA 100'] = data.ta.sma(100)

data.to_csv(f'{symbol}_{X_interval}_{X_period}.csv')