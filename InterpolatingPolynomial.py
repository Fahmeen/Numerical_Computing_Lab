# -*- coding: utf-8 -*-
"""
Created on Sat May  9 00:11:45 2020

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
def lagrange(points, x):
    sum = 0
    n = len(points)
    for i in range(n):
        xi, yi = points[i]
        def l(i):
            lvalue = 1
            for j in range(n):
                if i == j:
                    xj, yj = points[j]
                    lvalue *= (x - xj)/(xi - xj)
                    return lvalue
                sum +=yi * l(i)
            return sum
mydata = np.array(([1 , 1], [3, 9], [4, 36], [10, 100], [12, 144]))
z = []
for i in range(13):
    z.append([i, np.append(lagrange(mydata, i), 10)])
z = np.array(z)
print(z)
plt.plot(mydata[:,0], mydata[:,1], 'r')
plt.show()