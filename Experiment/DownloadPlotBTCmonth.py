import yfinance as yf
import pandas as pd
import pandas_ta as ta
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

## Defines timeframe to get data from
today = datetime.today()
one_month_ago = (today - timedelta(days=30)).strftime('%Y-%m-%d')

## pull data from yahoo finance ( 1 month back )
data = yf.download("BTC-USD", start=one_month_ago, end=today)

## these define what the graph will look like
## 'Date' not found in the df, because it was in the index, not a column. So we need to add it
data.plot(y='Adj Close')
plt.xlabel('Date')

##this displays the pre-defined graph
plt.show()
