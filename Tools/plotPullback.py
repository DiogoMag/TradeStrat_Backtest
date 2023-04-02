import random
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the starting price and volatility
start_price = 60000
volatility = 0.005

# Generate the price values
prices = [start_price]
for i in range(1, 20):
    last_price = prices[-1]
    next_price = last_price + (last_price * random.uniform(-volatility, volatility))
    prices.append(round(next_price, 2))

# Create the pandas DataFrame with only the relevant columns
df = pd.DataFrame({'#': range(1, 21), 'Price': prices})[['#', 'Price']]

# Create the plot using Seaborn
sns.set_style('darkgrid')
sns.lineplot(x='#', y='Price', data=df)
plt.title('Bitcoin Price with Higher Volatility')
plt.xlabel('Time')
plt.ylabel('Price')

# Identify and plot pullbacks
for i in range(1, len(prices)):
    if prices[i] < prices[i-1]:
        j = i + 1
        while j < len(prices) and prices[j] < prices[j-1]:
            j += 1
        plt.axvline(x=j-1, linestyle='--', color='green')

plt.show()
