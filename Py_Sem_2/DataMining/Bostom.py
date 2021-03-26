import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"Boston.csv")
data1 = np.asarray(data)
print(data1[0:])

"""  print(data.nrows[1])
 np.matrix(data)
 np.mean use to find mean from the given data set
 NOTE: axis = 0 is rows side and axis =1 is column side"""
# d = data.target
print(d)
data_mean = np.mean(data, axis=0)
print("Mean:\n", data_mean)
data_median = np.median(data, axis=0)
print("Median;\n", data_median)
data_std = np.std(data, axis=0)
print("STD:\n", data_std)
data_count = np.count_nonzero(data, axis=0)
print("Data Count\n", data_count)
data_variance = np.var(data, axis=0)
print("Data Variance:\n", data_variance)

cr = data.corr(method='pearson')
print(cr)
# cr.to_csv(r"correlation.csv")
# plt.style.use("ggplot")
# plt.rcParams["figure.figsize"] = (12,8)
# sns.scatterplot(x = data.sepal_length, y=data.sepal_width,
#                hue = data.species, style=data.species)