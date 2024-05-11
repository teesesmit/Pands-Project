# This program researches the Iris data set
# 1. Outputs a summary of each varaible to a single text file
# 2. Saves a histogram of each variable to png files
# 3. Outputs a scatter plot of each pair of variables.
# 4. Further analysis
# Author: Theresa Smyth

# Imports of data frames
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Loads the Iris dataset from a CSV file 
iris_dataset = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

# 1. Summary of each variable to a single test file

# Opens a file named "iris_summary.txt" in write mode ('w'). 'with' ensures that the file is properly closed.
# 'describe' generates stats of dataset, 'to_string' converts summary data to a string and writes it to a .txt file
# https://www.statology.org/pandas-to-text-file/ 
with open('iris_summary.txt', 'w') as df:
     df.write(iris_dataset.describe().to_string())
       
# Histogram of each variable to PNG files
# Loop through each numerical column in the dataset
for column in iris_dataset.select_dtypes(include=['float64', 'int64']).columns:
    # Create a seaborn histogram for the column
    # https://www.w3schools.com/python/numpy/numpy_random_seaborn.asp
    sns_plot = sns.histplot(iris_dataset[column], kde=False)
    
    # Set title and labels
    sns_plot.set_title(f'Histogram of {column}')
    sns_plot.set_xlabel(column)
    sns_plot.set_ylabel('Frequency')
    
    # Save the plot as a PNG file
    plt.savefig(f'{column}_histogram.png')
    
    # Clear the plot for the next iteration
    plt.clf()

