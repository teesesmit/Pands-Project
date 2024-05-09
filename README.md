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
    - Summary of each variable
In order to conduct analysis of the Iris dataset, the program needs to import two modules pandas and matplotlib.pyplot. [Pandas](https://www.w3schools.com/python/pandas/default.asp) is a Python library designed to analyze data and for managing datasets, facilitating tasks such as cleaning, exploration, and manipulation of data. It enables the examination of large datasets, assists in making them readble and supports the formation of conclusions based on statistical principles. [Matplotlib.pyplot](https://www.w3schools.com/python/matplotlib_intro.asp) is a low level graph plotting library i.e. histograms, scatter plots bar chasrts etc for python. In this program pandas is imported as 'pd' and matplotlib.pyplot as 'plt'.

The data must initially be loaded into the program to allow analysis to be preformed. The data set is saved within this directory in a Comma Separated Values[(CSVs)](https://realpython.com/lessons/what-are-csv-files/) format, a plain test file format commonly used for input/output of programs. Since the dataset is in CSV format, .[read_csv()](https://www.w3schools.com/python/pandas/pandas_csv.asp) is used to read the dataset and store it as a dataframe object in the variable iris_dataset.

To summarise each variable and create a single text file, the file has to be opened, data sumerised and written to a text file. In order to do this the open function is used along side the with statement. The [open()](https://www.w3schools.com/python/python_file_handling.asp) function along with the write parameter allows you to open and write the files, however the open() function must be used with the close() function. In order to have this completed without the close() function the [with](https://realpython.com/python-with-statement/) statment will close the file without being told. With the data loaded and opened, the [describe()](https://www.w3schools.com/python/pandas/ref_df_describe.asp) method returns the summary of each varible of the data in the dataframe. However, the write() method expects a string as an input, not a pandas dataframe. Hence, [.to_string()](https://www.geeksforgeeks.org/python-pandas-dataframe-to_string/) method converts the pandas dataframe to a string format that can be written to a text file.

    - Histogram of each variable
    - Scatter plot of each variable
    – Any other analysis appropriate
## Summary of :
    - Data
    – Histograms
    – Scatter plot
    – Any other analysis appropriate

## Technical information
    – What is required to runcode

## References - do i need these if embedded???

# Conclusion
Overall the Iris data set is a bunch of numbers that describe the Iris flowers features, like how big their petals and sepals are. It's a classic dataset used to teach people how to work with data and train machine learning models to recognize patterns and statistics. Linear Discriminant Analysis (LDA) helps to separate different species of iris flowers based on their measurements and simplifies the classification process by combining the measurements into a smaller set of variables.

## End

