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

# Loads the Iris dataset from a CSV file 
iris_dataset = pd.read_csv('iris.csv')

# Summary of each variable to a single test file
# Using 'with' to open files without needing to close files
# Converts summary data to a string and writes it to a .txt file 
with open('iris_summary.txt', 'w') as f:
     f.write(iris_dataset.describe().to_string())  
