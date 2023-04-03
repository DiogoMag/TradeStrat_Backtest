import pandas as pd
import pandas_ta as ta
import matplotlib as plt
import yfinance as yf
import time

df = pd.DataFrame()

data = yf.download("BTC-USD", start="2020-01-01", end="2020-12-31")

data.plot()
plt.show()