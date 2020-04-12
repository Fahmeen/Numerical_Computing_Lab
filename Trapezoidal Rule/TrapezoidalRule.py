# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 11:54:43 2020

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-0.5,1.5,100)
y = np.exp(-x**2)
plt.plot(x,y)

x0 = 0; x1 = 1;
y0 = np.exp(-x0**2); y1 = np.exp(-x1**2);
plt.fill_between([x0,x1],[y0,y1])

plt.xlim([-0.5,1.5]); plt.ylim([0,1.5]);
plt.show()
A = 0.5*(y1 + y0)*(x1 - x0)
print("Trapezoid area:", A)