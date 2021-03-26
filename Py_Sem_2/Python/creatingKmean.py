# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:27:34 2021

@author: vishal
"""
import math
import pandas as pd
import matplotlib.pyplot as plt
def calculateEcludianDistance(x,y):
    s = 0
    for i,j in enumerate(x):
        s += pow((x[i]-y[i]),2)
    return math.sqrt(s)
    
def findMean(list):
    s = 0
    cnt = 0
    a = 0
    b = 0
    for i in list:
        s+= i[0]
        cnt+=1
    a = s/cnt
    s = 0
    for i in list:
          s+= i[1]
    b = s/cnt
    return [a,b]
          
def addToCluster():
    for i in data:
        x = calculateEcludianDistance(i,clustermean[0])
        y = calculateEcludianDistance(i,clustermean[1])
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
    
    
df = pd.read_csv("E:\CodingZone\Python\Py_Sem_2\DataMining\MyData.csv")
data = df.values.tolist()
flag = [False]
cluster =[[[179,72]],[[183,72]]]
clustermean = []
clustermean.append(findMean(cluster[0]))
clustermean.append(findMean(cluster[1]))
for i in range(50):
    addToCluster()
    if(flag[0]):
        break
    if i != 49:
        cluster = [[],[]]
    




























