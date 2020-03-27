# -*- coding: utf-8 -*-
"""
@author: user
"""

def factorial(n):
    print("Factorial= " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print("Fact", n, " * factorial(" ,n-1, "): ",res)
        return res	

print(factorial(10))