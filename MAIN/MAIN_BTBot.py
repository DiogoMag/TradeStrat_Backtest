import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Set Variables
symbol= 'EURUSD'
sta_date= '2023-03-01'
end_date= '2023-04-01'
X_interval= '1wk'

# download data for EUR/USD for the specified dates
data = yf.download(f'{symbol}=X', start=sta_date, end=end_date, interval=X_interval)
data = data.drop(['Volume', 'Adj Close'], axis=1)

data.to_csv('TestData.csv')