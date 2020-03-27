# -*- coding: utf-8 -*-
"""
@author: user
"""

import numpy
import numpy as np
cvalues = [11, 22, 33, 44, 10, 20, 30, 40]
C = np.array(cvalues)
print(C)
print(C * 9 / 5 + 32)
fvalues = [ x*9/5 + 32 for x in cvalues] 
print(fvalues)
type(C)
