# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 20:41:45 2020

@author: user
"""

# Python3 code for implementation of Newton 
# Raphson Method for solving equations 
  
# An example function whose solution  
# is determined using Bisection Method.  
# The function is x^3 + x - 1 
def func( x ): 
    return (x * x * x) + (x) - 1
  
# Derivative of the above function  
# which is 3*x^x + 1 
def derivFunc( x ): 
    return (3 * x * x) + 1 
  
# Function to find the root 
def newtonRaphson( x ): 
    h = func(x) / derivFunc(x) 
    while abs(h) >= 0.0001: 
        h = func(x)/derivFunc(x) 
          
        # x(i+1) = x(i) - f(x) / f'(x) 
        x = x - h 
      
    print("The value of the root is : ", 
                             "%.4f"% x) 
  
# Driver program to test above 
x0 = -20 # Initial values assumed 
newtonRaphson(x0) 