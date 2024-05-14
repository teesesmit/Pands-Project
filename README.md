# Iris_Data_Set_Project

![Image 1](/320px-Iris_versicolor_3.jpeg)![Image 2](/Iris_virginica.jpeg)![Image 3](/Kosaciec_szczecinkowaty_Iris_setosa.jpeg)

## Table of Contents
* [Introduction](#introduction)
* [Project Program Description](#programming) 
* [Analysis](#analysis)
* [Technical Information](#technical-information)
* [Summary](#summary-of)

## **Introduction**
The [Iris flower data set](https://en.wikipedia.org/wiki/Iris_flower_data_set) is a collection of information about three distinct species of Iris flowers: Iris setosa, Iris versicolor, and Iris virginica. The Iris data set contains a set of 150 features measured from each sample: the lengths and widths of both sepals and petals measured in centimeters.

It was introduced and made famous by the British statistcian and biologist [Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher) as an example of [Linear discriminant analysis (LDA)](https://en.wikipedia.org/wiki/Linear_discriminant_analysis). LDA is a technique used in statistics that looks at the differences between the species of flowers and helps to find a straight line or plane that best seperates groups of data. This can be useful to predict the species of a new iris flower based on its measurements i.e. where in the plane it falls. Another valuable resource is its ability to deal with the analysis of multiple variables at the same time and their relationships with each other. 

## Programming
### Summary of each variable
In order to conduct analysis of the Iris dataset, the program needs to import modules pandas and matplotlib.pyplot. [Pandas](https://www.w3schools.com/python/pandas/default.asp) is a Python library designed to analyze data and for managing datasets, facilitating tasks such as cleaning, exploration, and manipulation of data. It enables the examination of large datasets, and assists in making them readable and supports the formation of conclusions based on statistical principles. [Matplotlib.pyplot](https://www.w3schools.com/python/matplotlib_intro.asp) is a low level graph plotting library i.e. histograms, scatter plots bar charts etc for python. In this program pandas is imported as 'pd' and matplotlib.pyplot as 'plt'.

The imported data is stored in a dataframe called iris, which contains information of 5 variables for 150 observations (flowers). While the first 4 variables/columns, Sepal.Length, Sepal.Width, Petal.Length, and Petal.Width, contain numeric values. The 5th variable/column, Species, contains characters indicating which sub-species a sample belongs to. Selecting the appropriate [variable]( https://www.data-to-viz.com/) is pivotal for accurately presenting and analyzing the data. The Iris dataframe is saved within this directory "Pands Project" as a Comma Separated Values[(CSVs)](https://realpython.com/lessons/what-are-csv-files/) format, a plain test file format commonly used for input/output of programs. Since the dataset is in CSV format, .[read_csv()](https://www.w3schools.com/python/pandas/pandas_csv.asp) is used to read the dataset.

To summarise each variable and create a single text file, the file has to be opened, data sumerised and written to a text file. In order to do this the open function is used along side the with statement. The [open()](https://www.w3schools.com/python/python_file_handling.asp) function along with the write parameter allows you to open and write the files, however the open() function must be used with the close() function. In order to have this completed without the close() function the [with](https://realpython.com/python-with-statement/) statment will close the file without being told. With the data loaded and opened, the [describe()](https://www.w3schools.com/python/pandas/ref_df_describe.asp) method returns the summary of each varible of the data in the dataframe. However, the write() method expects a string as an input, not a pandas dataframe, hence [.to_string()](https://www.geeksforgeeks.org/python-pandas-dataframe-to_string/) method converts the pandas dataframe to a string format that can be written to a text file.

### Histogram of each variable
Histograms are excellent ways for the visualization of large datasets to display the key features of its numeric contents in a clear straightforward manner. [Seaborn](https://seaborn.pydata.org) is a python visualization library based on matplotlib.pyplot, as referenced above matplotlib.pyplot is a collect of command style functions. These will be used in this section of the program to create the first 4 variables into histograms in python. This uses the hist() function which will read the arrays and produce a histogram. The sns.histplot function is versatile and allows extensive customization which allows for meaningful changes to assess the dataframe. In the code the 'def save_histogram' defines a function names 'save histograms' that does not take any arguments. Next the program iterates over each column in the dataframe except the last one using the '[:-1]'as that contains the target variable. This is done using slicing. The target variable is categorical, not continuous, therefore it cannot be made into a histogram. Once completed the histogram can be [created](https://www.datacamp.com/tutorial/how-to-make-a-seaborn-histogram) to preference. The histogram is then saved as a PNG file and the line save histograms is used to execute the code.

### Scatter plot of each variable
In this analysis we are also using the seaborn and matplotlib libraries to create visualizations in python. [Scatter plots](https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot) show points on a graph and each point represents data. Scatter plots identifies possible relationships between changes observed in different sets of variables. It provides a visual and statistical means to test the strenght of a relationship between two varaibles. The relationship between these variables can be shown for different subsets of the data using the [hue](https://seaborn.pydata.org/generated/seaborn.scatterplot.html), size and style parameters. Hue is the grouping varaible that will produce points with different colors. It can either be categorical or numeric. In this case, the groupings were Iris-setosa, Iris-versicolor and Iris-virginica.  

For the first scatter plot we are representing the 'sepal lenght' and sepal width' variables and the second 'petal lenght' and petal width' The points are coloured based on the species of the iris flower they represent. The legend makes it more readable. The axes 1 legend bbox_to_anchor parameter is used to add a legend to the second subplot and position it at the top-right corner of the plot.  

### Pairplot
[Pairplot](https://seaborn.pydata.org/generated/seaborn.pairplot.html) gives the better comparison and observation of the data and provides enough informations to draw conclusions.

For the pairplot again we use the seaborn and matplotlib libraries. The sns.pairplot, hue='species' part of the code generates a pairplot of the Iris dataset. A pairplot is a grid of scatterplots showing relationships between pairs of variables in a dataset. Assigning a hue variable adds a semantic mapping and changes the default marginal plot to a layered kernel density estimate (KDE) i.e the hue parameter is used to color the points based on the species variable, making it easier to distinguish different species in the plot.

## Summary of :
    - Data
    – Histograms
    – Scatter plot
    – Any other analysis appropriate

## Technical information
###  
* Visual Stuido Code
* python
* Anaconda

### Libraries to import
* import seaborn as sns
* import pandas as pd
* import numpy as np
* import matplotlib.pyplot as plt



# Conclusion
Overall the Iris data set is a bunch of numbers that describe the Iris flowers features, like how big their petals and sepals are. It's a classic dataset used to teach people how to work with data and train machine learning models to recognize patterns and statistics. Linear Discriminant Analysis (LDA) helps to separate different species of iris flowers based on their measurements and simplifies the classification process by combining the measurements into a smaller set of variables.

## End

