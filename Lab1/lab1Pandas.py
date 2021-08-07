#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../Lab2/Data/Datasets/Exercise-CarData.csv')
d = pd.crosstab(index=data['Index'], columns="Price", dropna=True)
print(d)

print(data.info())

# Count Total Null values in each column
print("Total Null Data:", data.isnull().sum())

# Finding the Histogram
# From the given dataset ‘mtcars.csv’, plot a histogram to check the frequency distributi
# on of the variable ‘mpg’ (Miles per gallon).
plt.hist(data['Age'], bins=5)
plt.show()

# scatter plot of ‘mpg’ (Miles per gallon) vs ‘wt’ (Weight of car)
plt.scatter(data['Age'], data['Price'])
plt.show()

# In the dataframe, under the variable gear count total records in each value
df = pd.DataFrame(data, columns=['Age'])
print("Count How many values:\n", df['Age'].value_counts())
