#importing some required libraries

import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn import tree
#Loading datasets
iris_data = load_iris()
iris=pd.DataFrame(iris_data.data)

#priting features name of iris data
print ("Features Name : ", iris_data.feature_names)

#shape of datasets
print ("Dataset Shape: ", iris.shape)

#first five sample
print ("Dataset: ",iris.head())

#priting samples and target
X = iris.values[:, 0:4]
Y = iris_data.target
print(X)
print(Y)

# Splitting the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state = 100)

# Decision tree classifier
clf= DecisionTreeClassifier(random_state = 100)

#fitting the training data
clf.fit(X_train, y_train)