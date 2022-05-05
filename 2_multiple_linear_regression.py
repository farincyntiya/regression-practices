# -*- coding: utf-8 -*-
"""2_Multiple_Linear_Regression

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZHPXFUU1ae0u4hd7weNix0clsGdzhdfJ

# 01. Import Libraries and Data
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#  from google.colab import drive
#  drive.mount('/content/gdrive')

dataset = pd.read_csv('50_Startups.csv')

dataset.head()

"""# Data Encoding"""

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

X

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

X

"""# 02. Data Splitting"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""# 03. Training Model"""

regressor = LinearRegression()
regressor.fit(X_train, y_train)

"""# 04. Predicting the Test Data"""

y_pred = regressor.predict(X_test)

y_pred

np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

"""# 05. Model Evaluation"""

regressor.score(X_train,y_train) # metric defaultnya adalah R-squared