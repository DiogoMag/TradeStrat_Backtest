
import pandas as pd
import pandas_ta as ta
import yfinance as yf

## pandas setting no max rows or columns displayed
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Define the ticker symbol and the start and end dates
ticker = "BTC"
start_date = "2022-01-01"
end_date = "2023-04-06"
timestamp = "2022-03-15"

# Download the historical data
df = yf.download(ticker, start=start_date, end=end_date, interval="1d")


# Calculate the MACD
df = df.ta.macd()

# Print the entire DataFrame
print(df)

# Select the MACD value for the specific timestamp
try:
    macd_value = df.loc[timestamp, "MACD"]
    print(f"MACD value for {timestamp}: {macd_value}")
except KeyError:
    print(f"No MACD value found for {timestamp}")

