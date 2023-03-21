import yfinance as yf
import pandas as pd
import pandas_ta as ta
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame()

data = yf.download("BTC-USD", start="2020-01-01", end="2020-12-31")
data
data.plot()
sns.lineplot(data=data, x="Date", y="Open")
plt.show()
