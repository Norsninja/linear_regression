import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
df = pd.read_csv('dog_data.csv')

# Create a figure with 3 subplots
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))

# Plot a histogram in the first subplot
ax1.hist(df['cost_per_pound'], bins=20)
ax1.set_xlabel('Cost per pound')
ax1.set_ylabel('Frequency')
ax1.set_title('Histogram')

# Plot a box plot in the second subplot
ax2.boxplot(df['cost_per_pound'])
ax2.set_xlabel('Cost per pound')
ax2.set_title('Box Plot')

# Plot a scatter plot in the third subplot
ax3.scatter(df['dog_size'], df['cost_per_pound'])
ax3.set_xlabel('Dog size')
ax3.set_ylabel('Cost per pound')
ax3.set_title('Scatter Plot')

plt.show()