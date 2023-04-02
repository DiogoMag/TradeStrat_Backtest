import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create static dataframe
data = {'#': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        'Price': [60000, 60250, 60500, 60200, 60150, 59900, 60200, 60550, 60800, 60600, 60500, 60850,
                  61100, 61350, 61000, 60650, 60700, 60950, 61200, 61450]}

df = pd.DataFrame(data=data)

# Plot with seaborn
sns.lineplot(data=df, x="#", y="Price")

# Display plot
plt.show()
