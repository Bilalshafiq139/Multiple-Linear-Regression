# -*- coding: utf-8 -*-
"""Multiple Linear Regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Lh3VUfWcaJS0iGSfXHjxP3VNOb-hODXn

# Do you think if scaling is necessary for horsepower, engine_size, and weight?

Yes I think it is required becuse of the large differenc all these 3 column values
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('multiple_linear_regression_data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

dataset.head()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train[:, :-1] = sc.fit_transform(X_train[:, :-1])
X_test[:, :-1] = sc.transform(X_test[:, :-1])

X_test

X_train

y_train

y_test

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred=regressor.predict(X_test)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

regressor.predict([[0, -1, 30]])

