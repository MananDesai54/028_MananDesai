#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../Lab2/Data/Datasets/Data_for_Transformation.csv")
d = pd.crosstab(index=data['Country'], columns='Age', dropna=True)
print(d)

plt.scatter(data['Age'], data['Salary'])
plt.show()

plt.hist(data['Salary'], bins=5)
plt.show()

plt.bar(data['Country'], data['Age'])
plt.show()
