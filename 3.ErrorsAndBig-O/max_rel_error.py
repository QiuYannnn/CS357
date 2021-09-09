# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 15:50:08 2021

@author: Einsgate
"""

import numpy as np

n = 5
predicted = np.array([4,5,4,5,4])

actual = np.array([5,4,5,4,5])
error_array = np.empty(n)

for i in range(n):
    error = abs(predicted[i] - actual[i]) / actual[i]
    error_array[i] = error
max_rel_error = error_array.max()
print(max_rel_error)