from sklearn.datasets import load_boston
import numpy as np
import pandas as pd
boston = load_boston()
# print(boston)
# print(boston.feature_names)


# Converting data from nd-array to dataframe and adding feature names to the data/\
data = pd.DataFrame(boston.data)
data.columns = boston.feature_names
data['MEDV'] = boston.target
x = boston.data
print(x)
print(data.head())
print(data.describe())
print(data['CRIM'])
