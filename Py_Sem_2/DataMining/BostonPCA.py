
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_boston
from sklearn.decomposition import PCA
pca=PCA(n_components=7)
boston = load_boston()
# print(boston.keys())
# print(boston['feature_names'])
df_boston = pd.DataFrame(boston["data"],columns=boston['feature_names'])
# print(df_boston)
scaler = StandardScaler()
scaler.fit((df_boston))
# print(df_boston)
scaled_data = scaler.transform(df_boston)
# print(scaled_data)
pca.fit(scaled_data)
x_pca=pca.transform(scaled_data)
print(x_pca)