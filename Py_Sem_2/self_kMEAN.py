# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:27:34 2021

@author: vishal
"""
import math
def calculateEcludianDistance(x,y):
    return math.sqrt(pow((x[0]-y[0]),2)-pow((x[1]-y[1]),2))
    
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
    clustermean[0] = findMean(cluster[0])
    clustermean[1] = findMean(cluster[1])
    
data = [[185,72],
        [170,72],
        [168,72],
        [179,72],
        [182,72],
        [188,72],
        [180,72],
        [180,72],
        [183,72],
        [180,72],
        [180,72],
        [177,72],
        ]
cluster =[[[179,72]],[[183,72]]]
clustermean = []
clustermean.append(findMean(cluster[0]))
clustermean.append(findMean(cluster[1]))

addToCluster()

cluster = [[],[]]

addToCluster()




























