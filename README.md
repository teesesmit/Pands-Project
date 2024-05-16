# Iris_Data_Set_Project

![Image 1](/320px-Iris_versicolor_3.jpeg)![Image 2](/Iris_virginica.jpeg)![Image 3](/Kosaciec_szczecinkowaty_Iris_setosa.jpeg)

## Table of Contents
* [Introduction](#introduction)
* [Project Program Description](#programming) 
* [Analysis](#analysis-of-data)
* [Technical Information](#technical-information)
* [Summary](#summary-of)

## **Introduction**
The [Iris flower data set](https://en.wikipedia.org/wiki/Iris_flower_data_set) is a collection of information about three distinct species of Iris flowers: Iris setosa, Iris versicolor, and Iris virginica. The Iris data set contains a set of 150 features measured from each sample: the lengths and widths of both sepals and petals measured in centimeters.

It was introduced and made famous by the British statistcian and biologist [Ronald Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher) as an example of [Linear discriminant analysis (LDA)](https://en.wikipedia.org/wiki/Linear_discriminant_analysis). LDA is a technique used in statistics that looks at the differences between the species of flowers and helps to find a straight line or plane that best seperates groups of data. This can be useful to predict the species of a new iris flower based on its measurements i.e. where in the plane it falls. Another valuable resource is its ability to deal with the analysis of multiple variables at the same time and their relationships with each other. 

## Programming
### Summary of each variable
In order to conduct analysis of the Iris dataset, the program needs to import modules pandas and matplotlib.pyplot. [Pandas](https://www.w3schools.com/python/pandas/default.asp) is a Python library designed to analyze data and for managing datasets, facilitating tasks such as cleaning, exploration, and manipulation of data. It enables the examination of large datasets, and assists in making them readable and supports the formation of conclusions based on statistical principles. [Matplotlib.pyplot](https://www.w3schools.com/python/matplotlib_intro.asp) is a low level graph plotting library i.e. histograms, scatter plots, bar charts etc for python. In this program pandas is imported as 'pd' and matplotlib.pyplot as 'plt'.

The imported data is stored in a dataframe called iris, which contains information of 5 variables for 150 observations (flowers). While the first 4 variables/columns, Sepal.Length, Sepal.Width, Petal.Length, and Petal.Width, contain numeric values. The 5th variable/column, Species, contains characters indicating which sub-species a sample belongs to. Selecting the appropriate [variable]( https://www.data-to-viz.com/) is pivotal for accurately presenting and analyzing the data. The Iris dataframe is saved within this directory "Pands Project" as a Comma Separated Values[(CSVs)](https://realpython.com/lessons/what-are-csv-files/) format, a plain test file format commonly used for input/output of programs. Since the dataset is in CSV format, .[read_csv()](https://www.w3schools.com/python/pandas/pandas_csv.asp) is used to read the dataset.

To summarise each variable and create a single text file, the file has to be opened, data sumerised and written to a text file. In order to do this the open function is used along side the with statement. The [open()](https://www.w3schools.com/python/python_file_handling.asp) function along with the write parameter allows you to open and write the files, however the open() function must be used with the close() function. In order to have this completed without the close() function the [with](https://realpython.com/python-with-statement/) statment will close the file without being told. With the data loaded and opened, the [describe()](https://www.w3schools.com/python/pandas/ref_df_describe.asp) method returns the summary of each varible of the data in the dataframe. However, the write() method expects a string as an input, not a pandas dataframe, hence [.to_string()](https://www.geeksforgeeks.org/python-pandas-dataframe-to_string/) method converts the pandas dataframe to a string format that can be written to a text file.

### Histogram of each variable
Histograms are excellent ways for the visualization of large datasets to display the key features of its numeric contents in a clear straightforward manner. [Seaborn](https://seaborn.pydata.org) is a python visualization library based on matplotlib.pyplot, as referenced above matplotlib.pyplot is a collection of command style functions. These will be used in this section of the program to create the first 4 variables into histograms in python. This uses the hist() function which will read the arrays and produce a histogram. The sns.histplot function is versatile and allows extensive customization which allows for meaningful changes to assess the dataframe. In the code the 'def save_histogram' defines a function names 'save histograms' that does not take any arguments. Next the program iterates over each column in the dataframe except the last one using the '[:-1]'as that contains the target variable. This is done using slicing. The target variable is categorical, not continuous, therefore it cannot be made into a histogram. Once completed the histogram can be [created](https://www.datacamp.com/tutorial/how-to-make-a-seaborn-histogram) to preference. The histogram is then saved as a PNG file and the line save histograms is used to execute the code.

### Scatter plot of each variable
In this analysis we are also using the seaborn and matplotlib libraries to create visualizations in python. [Scatter plots](https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot) show points on a graph and each point represents data. Scatter plots identifies possible relationships between changes observed in different sets of variables. It provides a visual and statistical means to test the strenght of a relationship between two varaibles. The relationship between these variables can be shown for different subsets of the data using the [hue](https://seaborn.pydata.org/generated/seaborn.scatterplot.html), size and style parameters. Hue is the grouping varaible that will produce points with different colors. It can either be categorical or numeric. In this case, the groupings were Iris-setosa, Iris-versicolor and Iris-virginica.  

For the first scatter plot we are representing the 'sepal lenght' and sepal width' variables and the second 'petal lenght' and petal width' The points are coloured based on the species of the iris flower they represent. The legend makes it more readable. The axes 1 legend bbox_to_anchor parameter is used to add a legend to the second subplot and position it at the top-right corner of the plot.  

### Pairplot
[Pairplot](https://seaborn.pydata.org/generated/seaborn.pairplot.html) gives the better comparison and observation of the data and provides enough information to draw conclusions. For the pairplot again we use the seaborn and matplotlib libraries. The sns.pairplot, hue='species' part of the code generates a pairplot of the Iris dataset. A pairplot is a grid of scatterplots showing relationships between pairs of variables in a dataset. Assigning a hue variable adds a semantic mapping and changes the default marginal plot to a layered kernel density estimate (KDE) i.e the hue parameter is used to color the points based on the species variable, making it easier to distinguish different species in the plot.

## Analysis of data
### Data Summary
The fist section of the analysis is the summary of [data](iris_summary.txt) which visualizes the count of each column along with their average value, standard diviation, minimum and maximum values. This produces alot of useful information about the distrubution of each variable. For example for petal lenght, the minimum lenght is 1.0cm, the maximum is 6.9cm and the avaerage petal lenght is 3.8cm. The 1st quartile (25th percentile) is 1.6cm. This tells us that only 25% of the flowers have petals shorter than 1.6cm. The 3rd quartile (75th percentile) is 5.1cm, as 75% of the flowers have petals shorter then 5.1cm. These summary statistics are graphically represented in the histograms, scatter plots and pair plots within this project.

### Histograms
Histograms show the distribution of data by plotting the frequency of data in bins. The histogram for [petal lenght](petal_lenght_histogram.png) shows that there are more flowers with petal lenghts between 1cm and 1.5cm. The distribution of this data appears to be bimodal, indicating that there are two distinct values that occur with the highest frequency, rather than a single value. Instead of having a single peak where most data points are concentrated, there are two peaks.  This suggests that the data might be coming from two different sources or groups i.e. species, each with its own central tendency. The highest frequency of [petal width](petal_width_histogram.png) is below 35 which is roughly between 0.1 and 0.2cm. There is a noticeable difference in the histograms when observing the sepal variables. The highest frequency for [sepal width](sepal_width_histogram.png) is slightly above 25, which is approximately 3cm. The distribution of sepal width is nearly symmetric and unimodal. This is similiar to [sepal lenght](sepal_lenght_histogram.png) where the distrubution is skewed slightly to the left where there are two point fighting for the highest freqency. 

### Scatter plot
[Scatter plots](Scatter_Plots.png) are highly effective for visualizing the correlation between two numerical columns. For instance, plotting petal width against petal length reveals a positive correlation: flowers with longer petals often have wider ones. This indicates that petal dimensions tend to increase together. Another notable feature is the presence of two distinct clusters of points, clearly identifying that the smaller cluster in the lower left as the setosa species. The other two species also exhibit some separation in this plot though less distinctly. This provides valuable insight into the dataset, is there something about the evnvironment that may be keeping the setosa species smaller. Versicolor species lies in the middle of the other two species in terms of sepal lenght and widht. Setosa has the smaller sepal lenghts but larger sepal widths where Virginica has larger sepal lenghts but smaller sepal widths.  

### Pairplot
[Pair plots](pairplot.png) are a group of scatterplots which enables the visualization of the relationship between each two pairs of variables in the dataset. In these plots we can analyse sepal lenght versus petal lenght and sepal width verses petal width. Setosa data points are well seperated having shorter petals and smaller sepal lenghts compared to the other species. Virginica generally have larger measurements for both sepal and petal dimensions similiar to Versicolor. The linear relationships in these plots are also more pronounced compared to sepal length vs. sepal width. 

### Technical information
* Visual Stuido Code
* python
* Anaconda
* import seaborn as sns
* import pandas as pd
* import numpy as np
* import matplotlib.pyplot as plt

## Conclusion
The Iris dataset is a classic dataset used to teach people how to work with data and train machine learning models to recognize patterns and statistics. Linear Discriminant Analysis (LDA) helps to separate different species of iris flowers based on their measurements and simplifies the classification process by combining the measurements into a smaller set of variables. Overall the Iris data set is a bunch of numbers that describe the Iris flowers features, like how big their petals and sepals are. Iris dataset has clear clusters for the setosa species, while versicolor and virginica are more similar but still separable, especially when considering petal measurements.  

## End

