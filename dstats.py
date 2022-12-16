import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
df = pd.read_csv('dog_data.csv')

# Calculate and print some descriptive statistics
print(f'Mean: {df["cost_per_pound"].mean()}')
print(f'Median: {df["cost_per_pound"].median()}')
print(f'Standard deviation: {df["cost_per_pound"].std()}')
print(f'Minimum: {df["cost_per_pound"].min()}')
print(f'Maximum: {df["cost_per_pound"].max()}')

# Plot a histogram of the data
plt.hist(df['cost_per_pound'], bins=20)
plt.xlabel('Cost Per Pound')
plt.ylabel('frequency')
plt.show()
