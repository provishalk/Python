from sklearn.datasets import load_boston
import numpy as np
import pandas as pd
X, y = load_boston(return_X_y=True)
df = pd.DataFrame(X)
print(df.head())
#print(X)
cor_matrix = df.corr().abs()
upper_tri = cor_matrix.where(np.triu(np.ones(cor_matrix.shape),k=1).astype(np.bool))
to_drop = [column for column in upper_tri.columns if any(upper_tri[column] > 0.62)]
print(); print(to_drop)
df1 = df.drop(df.columns[to_drop], axis=1)
print(); print(df1.head())