# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 16:47:30 2021

@author: visha
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

# read the image
image = cv2.imread("frame2.jpg")

# convert to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# reshape the image to a 2D array of pixels and 3 color values (RGB)
pixel_values = image.reshape((-1, 3))
# convert to float
pixel_values = np.float32(pixel_values)
data = pixel_values.tolist()