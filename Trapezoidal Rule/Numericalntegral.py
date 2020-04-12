# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:16:20 2020

@author: user
"""

#import
from math import sin,pi
#defining function
f = lambda x: x * sin(x)
#defining limit
a = 0 #Lower limit
b = pi/2 #Upper limit
#Number of division
n=5
#Step size
h = (b - a)/n
#Formula
s = 0.5 * (f(a) + f(b))
#loop
for i in range(1, n):
    s += f(a + i * h)
    Integral = h* 5
    #Output
    print('Integral = %f' %Integral) 