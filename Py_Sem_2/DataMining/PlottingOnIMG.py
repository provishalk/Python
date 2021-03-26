# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 15:53:48 2021

@author: visha
"""

import matplotlib.pyplot as plt
import numpy as np
xyz=np.array(np.random.random((100,3)))
plt.scatter(xyz[:,0], xyz[:,1])
plt.title("Point observations")
plt.xlabel("Easting")
plt.ylabel("Northing")
marker_size=15
plt.scatter(xyz[:,0], xyz[:,1], marker_size)
plt.show()