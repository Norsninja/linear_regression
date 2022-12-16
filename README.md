## Linear Regression and Random Data Generation

This repository contains two Python files:

linear_regression.py: a script that uses univariate linear regression to fit a line to a set of data points and plot the results.
generate_random_data.py: a script that generates random data points that follow a linear pattern and writes the data to a CSV file.
Linear Regression

The linear_regression.py script uses the scikit-learn library to perform univariate linear regression on a set of data points. It reads the data from a CSV file, fits a line to the data using the LinearRegression model, and plots the data and the fitted line.

To use the script, run the following command:

python linear_regression.py data.csv

where data.csv is the path to the CSV file containing the data.

## Random Data Generation

The generate_random_data.py script generates random data points that follow a linear pattern and writes the data to a CSV file. The slope and intercept of the linear pattern are randomly generated. The range of possible values for the x and y variables can be adjusted by changing the values of x_min, x_max, y_min, and y_max

To use the script, run the following command:

python generate_random_data.py data.csv

where data.csv is the path to the CSV file where the data will be written. The script will generate 50 random data points and write them to the CSV file. The file will have a header row with the column names dog_size and cost_per_pound.

A Large Language model trained by OpenAI, wrote both the linear regression and random data generation scripts in this repository. I just prompted and coached the reponse. I am a human bean that is still at the pre amateur coding level
