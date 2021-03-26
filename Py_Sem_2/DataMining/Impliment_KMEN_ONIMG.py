# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:54:09 2021

@author: Vishal Kumar
"""
import cv2
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
def calculateEcludianDistance(x,y):
    s = 0
    for i,j in enumerate(x):
        s += pow((x[i]-y[i]),2)
    return math.sqrt(s)
def calculateCityDistance(x,y):
    
    s = max(abs(x[0]-y[0]),abs(x[1]-y[1]),abs(x[2]-y[2]))
    return s


def findMean(list):
    s = 0
    cnt = 0
    a = 0
    b = 0
    c = 0
    for i in list:
        s+= i[0]
        cnt+=1
    a = s/cnt
    s = 0
    for i in list:
          s+= i[1]
    b = s/cnt
    s = 0
    for i in list:
          s+= i[2]
    c = s/cnt
    s = 0
    return [a,b,c]

def addToCluster():
    for i in data:
        x = calculateCityDistance(i,clustermean[0])
        y = calculateCityDistance(i,clustermean[1])
        if(x<y):
            cluster[0].append(i)
        else:
            cluster[1].append(i)
    a = clustermean[0]
    b = clustermean[1]
    clustermean[0] = findMean(cluster[0])
    clustermean[1] = findMean(cluster[1])
    if(a==clustermean[0] and b==clustermean[1]):
        flag[0] = True
        


# read the image
image = cv2.imread("frame2.jpg")

# convert to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# reshape the image to a 2D array of pixels and 3 color values (RGB)
pixel_values = image.reshape((-1, 3))
# convert to float
pixel_values = np.float32(pixel_values)


data = pixel_values.tolist()
flag = [False]
cluster =[[[41,41,41]],[[38,38,38]]]
clustermean = []
clustermean.append(findMean(cluster[0]))
clustermean.append(findMean(cluster[1]))

for i in range(100):
    addToCluster()
    if(flag[0]):
        break
    if i != 99:
        cluster = [[],[]]

c1 = np.array(cluster[0])
c2 = np.array(cluster[1])
plt.scatter(c1[:,0], c1[:,1], c=c1[:,1])
plt.scatter(c2[:,0], c2[:,1], c=c2[:,2])
plt.show()



















