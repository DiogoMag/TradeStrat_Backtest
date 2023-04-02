import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import random

# Generate the prices
start_price = 60000
volatility = 0.005
prices = [start_price]
for i in range(1, 20):
    last_price = prices[-1]
    next_price = last_price + (last_price * random.uniform(-volatility, volatility))
    prices.append(round(next_price, 2))

# Create a pandas DataFrame
df = pd.DataFrame({"#": range(1, 21), "Price": prices})

# Create the plot
sns.set_style("darkgrid")
sns.lineplot(x="#", y="Price", data=df)
plt.title("Bitcoin Price with Higher Volatility")
plt.xlabel("Time")
plt.ylabel("Price")
plt.show()
