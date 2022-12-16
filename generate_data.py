import random

# Set the range of possible values for x and y
x_min = 10
x_max = 150
y_min = 0.5
y_max = 3.0

# Generate a random slope and intercept for the linear equation
slope = random.uniform(-5, 5)
intercept = random.uniform(-5, 5)

# Define a linear function using the random slope and intercept
def linear_function(x):
    return slope * x + intercept

# Generate a random list of x values
x_values = [random.uniform(x_min, x_max) for _ in range(50)]

# Generate a corresponding list of y values using the linear function
y_values = [linear_function(x) for x in x_values]

# Add random noise to the y values
noise_range = 0.9  # the range of possible noise values
noise = [random.uniform(-noise_range, noise_range) for _ in range(50)]
y_values = [y + n for y, n in zip(y_values, noise)]

# Zip the lists together to create a list of (x, y) tuples
data = list(zip(x_values, y_values))

# Add the header row to the data
data = [('dog_size', 'cost_per_pound')] + data

# Write the data to a CSV file
import csv

with open('dog_data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
