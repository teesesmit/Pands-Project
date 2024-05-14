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

# Data Loading: Print the first few rows of the dataset
iris_dataset.head()

# 1. Summary of each variable to a single test file

# Opens a file named "iris_summary.txt" in write mode ('w'). 'with' ensures that the file is properly closed.
# 'describe' generates stats of dataset, 'to_string' converts summary data to a string and writes it to a .txt file
# https://www.statology.org/pandas-to-text-file/ 
with open('iris_summary.txt', 'w') as df:
     df.write(iris_dataset.describe().to_string())

# 2. Function to save histogram of each variable to PNG files
def save_histograms():
    # Iterate over each numerical column in the dataset
    for column in iris_dataset.columns[:-1]:  # Exclude the target variable
        # Create a histogram plot
        # https://www.datacamp.com/tutorial/how-to-make-a-seaborn-histogram
        plt.figure(figsize=(8, 6))
        sns.histplot(iris_dataset[column], kde=False, bins=20, color='skyblue')
        plt.title(f'Histogram of {column}', fontsize=16)
        plt.xlabel(column, fontsize=14)
        plt.ylabel('Frequency', fontsize=14)
        plt.grid(True)
        # Save the plot as a PNG file
        plt.savefig(f'{column}_histogram.png')
        plt.close()

# Call the function to save histograms
save_histograms()

# 3. Scatter plot of each pair of variables
# Create a figure with a 1x2 grid of subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Plot the Sepal scatterplot in the first subplot
# Seperates the 3 different species (grouping varaible)
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=iris_dataset, ax=axes[0])
axes[0].legend(bbox_to_anchor=(1, 1), loc='upper left')
axes[0].set_title('Sepal Scatter Plot')

# Plot the Petal scatterplot in the second subplot
sns.scatterplot(x='petal_length', y='petal_width', hue='species', data=iris_dataset, ax=axes[1])
axes[1].legend(bbox_to_anchor=(1, 1), loc='upper left')
axes[1].set_title('Petal Scatter Plot')

plt.tight_layout()
plt.savefig('Scatter_Plots.png')  # Save figure as a PNG file

# 4. Function to create and save pairplot
def save_pairplot():
    # Create pairplot
    sns.pairplot(iris_dataset, hue='species')
    # Save the plot as a PNG file
    plt.savefig('pairplot.png')
    plt.close()

# Call the function to create and save pairplot
save_pairplot()

                        


