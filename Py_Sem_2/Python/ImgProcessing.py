# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 10:17:51 2021

@author: vishal
"""
from skimage.io import imread ,imshow
import matplotlib.pyplot as plt
#matplotlib inline

img_gray = imread('E:\CodingZone\Python\Py_Sem_2\Python\img.jpg',as_gray=True)

print(img_gray.shape)
imshow(img_gray)


