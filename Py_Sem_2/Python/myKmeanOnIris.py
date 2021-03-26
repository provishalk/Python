# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 13:54:09 2021

@author: vishal
"""
import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
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
    c = 0
    d = 0
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
          s+= i[1]
    c = s/cnt
    s = 0
    for i in list:
          s+= i[1]
    d = s/cnt
    return [a,b,c,d]
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
df = pd.read_csv("E:\CodingZone\Python\Py_Sem_2\DataMining\Irisdata.csv")
data = df.values.tolist()
flag = [False]
cluster =[[[5.1,3.5,1.4,0.2]],[[5.4,3.9,1.7,0.5]]]
clustermean = []
clustermean.append(findMean(cluster[0]))
clustermean.append(findMean(cluster[1]))

for i in range(100):
    addToCluster()
    if(flag[0]):
        break
    if i != 99:
        cluster = [[],[]]


#---------------------------------------------#

x=np.array(cluster[0])
y=np.array(cluster[1])
c1= np.array(clustermean)
plt.scatter(x[:,0], x[:,1])
marker_size=15
marker=50
plt.scatter(x[:,0], x[:,1], marker_size,'r')
plt.scatter(y[:,0], y[:,1], marker_size,'g')
plt.scatter(c1[:,0], c1[:,1], marker,'black')
plt.show()





















