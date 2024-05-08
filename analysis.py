# This program researches the Iris data set
# 1. Outputs a summary of each varaible to a single text file
# 2. Saves a histogram of each variable to png files
# 3. Outputs a scatter plot of each pair of variables.
# 4. Further analysis
# Author: Theresa Smyth

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loads the Iris dataset from a CSV file
iris_data = pd.read_csv('/Users/Theresa/Desktop/Pands Project/iris.csv')
