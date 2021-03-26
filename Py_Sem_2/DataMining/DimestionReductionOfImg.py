# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 20:47:29 2021

@author: vishal
"""
import cv2

img = cv2.imread('E:\CodingZone\Python\Py_Sem_2\DataMining\WP_000084.jpg')

scale_percent = 0.25
print("old Dimensions: ",img.shape)
width = int(img.shape[1]*scale_percent)
height = int(img.shape[0]*scale_percent)
dimenstion=(width,height)
resized = cv2.resize(img,dimenstion,interpolation=cv2.INTER_AREA)
print("New Dimensions: ",resized.shape)
cv2.imshow('output',resized)
cv2.imwrite('newimg1.jpg',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
