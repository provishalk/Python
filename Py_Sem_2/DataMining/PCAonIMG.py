# Importing required libraries
import PIL
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
#importing img
img = cv2.imread('E:\CodingZone\Python\Py_Sem_2\DataMining\Ronak.JPG')

plt.imshow(img)


blue,green,red = cv2.split(img) 

#initialize PCA with first 20 principal components
pca = PCA(20)
 
#Applying to red channel and then applying inverse transform to transformed array.
red_transformed = pca.fit_transform(red)
red_inverted = pca.inverse_transform(red_transformed)
 
#Applying to Green channel and then applying inverse transform to transformed array.
green_transformed = pca.fit_transform(green)
green_inverted = pca.inverse_transform(green_transformed)
 
#Applying to Blue channel and then applying inverse transform to transformed array.
blue_transformed = pca.fit_transform(blue)
blue_inverted = pca.inverse_transform(blue_transformed)

img_compressed = (np.dstack((red_inverted, red_inverted, red_inverted))).astype(np.uint8)

plt.imshow(img_compressed)


cv2.imwrite('Ronak.jpg', img_compressed)

