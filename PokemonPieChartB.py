# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 22:30:40 2020

@author: user
"""

import pandas as pd

pokemon = ['Pikachu', 'Cosmic Eclipse', 'Unified Minds', 'Lost Thunder']
series = pd.Series([20, 30, 40, 10], 
                   index=pokemon, 
                   name='series')

series.plot.pie(figsize=(6, 6))
