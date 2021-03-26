import matplotlib.image as mplib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
# Reading an image and printing the shape of the image.
img = mplib.imread('E:\CodingZone\Python\Py_Sem_2\DataMining\WP_000084.jpg')
print(img.shape)
plt.imshow(img)
img_r = np.reshape(img, (1632, 1224, 3))
print(img_r.shape)
pca = PCA(32).fit(img_r)
img_transformed = pca.transform(img_r)
print(img_transformed.shape)
print(np.sum(pca.explained_variance_ratio_) )

# Retrieving the results of the image after Dimension reduction.
temp = pca.inverse_transform(img_transformed)
print(temp.shape)
temp = np.reshape(temp, (1632, 1224, 3))
print(temp.shape)
plt.imshow(temp)