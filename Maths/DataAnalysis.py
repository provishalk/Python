# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:46:28 2020

@author: visha
"""

import pandas as pd
import numpy as np
mydata = pd.read_csv('E:/VIT Course/Semester 1/1001 (Applied Mathematics And Statistical Methods)/Class Activity/Diabetes.csv')
mydata.info()
#print(mydata.head())
#print(mydata.tail())
mydata = mydata.fillna(0)
print()
Diabetes = mydata[["Glucose","BMI","Age","Outcome"]]
print(Diabetes.head())
print(Diabetes.describe())
print(Diabetes.columns[:])
print(Diabetes.columns[:-1])
print("++++++++++++++++++++")
print(Diabetes[Diabetes.columns[:-1]]==0)
print("++++++++++++++++++++")
print((Diabetes[Diabetes.columns[:-1]]==0).any(axis=1))
Diabetes1 = Diabetes.loc[~(Diabetes[Diabetes.columns[:-1]]==0).any(axis=1)]
Diabetes2 = Diabetes.loc[(Diabetes[Diabetes.columns[:-1]]==0).any(axis=1)]
print("++++++++++++++++++++")
print(Diabetes1)
print(Diabetes1.groupby("Outcome").mean())
print(Diabetes1.groupby("Outcome").agg({"Glucose":"mean","BMI":"median","Age":"sum"}))

print(Diabetes1.groupby("Outcome").agg(["mean","median"]))