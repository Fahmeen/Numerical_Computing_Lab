# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:01:10 2020
@author: user
"""
# Python3 program for implementation 
# of Lagrange's Interpolation 
# To represent a data point corresponding to x and y = f(x) 
class Data: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
def interpolate(f: list, xi: int, n: int) -> float:   
    # Initialize result 
    result = 0.0
    for i in range(n):   
        # Compute individual terms of above formula 
        term = f[i].y 
        for j in range(n): 
            if j != i: 
                term = term * (xi - f[j].x) / (f[i].x - f[j].x)   
        # Add current term to result 
        result += term   
    return result   
# Driver Code 
if __name__ == "__main__":   
    # creating an array of 4 known data points 
    f = [Data(3, 10), Data(9, 33), Data(10, 40), Data(14, 41)] 
    print("Value of f(11) is :", interpolate(f, 11, 4))   