import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the data from the CSV file
df = pd.read_csv('dog_data.csv')

# Extract the X and y values from the DataFrame
X = df['dog_size'].values.reshape(-1, 1)  # reshape to make it a 2D array
y = df['cost_per_pound'].values

# Create the linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Plot the data and the model's prediction
plt.scatter(X, y)
plt.plot(X, model.predict(X), color='red')
plt.title('Dog Prices')
plt.xlabel('dog size in lbs')
plt.ylabel('cost per pound')
plt.show()

# Make a prediction using gradient descent
x_new = [[x]]  # reshape to make it a 2D array
y_pred = model.predict(x_new)

# Plot the prediction on the graph
plt.scatter(X, y)
plt.plot(X, model.predict(X), color='red')
plt.scatter(x_new, y_pred, color='green')
plt.show()