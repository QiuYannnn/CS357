# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 13:21:24 2021

@author: Einsgate
"""

import numpy as np
price = np.array([10,20,30,40,50])
delta_price = np.array([1,2,1.0,2,1])
total_Clara = 158.0

total_meijer = price.sum()
total_error = delta_price.sum()

error1 = abs(total_Clara - (total_meijer - total_error))
error2 = abs(total_Clara - (total_meijer + total_error))

abs_error = min(error1, error2)