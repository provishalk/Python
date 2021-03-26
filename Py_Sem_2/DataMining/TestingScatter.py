# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 22:55:06 2021

@author: visha
"""

import matplotlib.pyplot as plt
import numpy as np
xyz=np.array(np.random.random((100,3)))
marker_size=15
plt.scatter(xyz[:,0], xyz[:,1], c=xyz[:,2])
plt.show()