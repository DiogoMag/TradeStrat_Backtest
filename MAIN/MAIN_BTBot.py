# Import the yfinance. If you get module not found error the run !pip install yfinance from your Jupyter notebook
import yfinance as yf

# Get the data for the stock AAPL
data = yf.download('AAPL','2023-03-23','2023-04-23')

# Import the plotting library
import matplotlib.pyplot as plt

# Plot the close price of the AAPL
data['Adj Close'].plot()
plt.show()