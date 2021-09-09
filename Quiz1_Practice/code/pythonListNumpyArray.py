# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 17:57:49 2021

@author: Einsgate
"""
import numpy as np
python_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
num_columns = 4
def transformer(python_list, num_columns):
    """ python_list: list, list object to be transformed
        num_columns: int, number of columns in the resulting numpy array
        return: 2D numpy array
    """
    # Your code starts here
    arr = np.array([[]])
    num_rows = len(python_list) / num_columns
    k = 0
    for i in range(num_rows):
        temp = []
        for j in range(num_columns):
            temp.append(python_list[k])
            k = k + 1
        arr = np.append(temp)
    return arr
    pass
print(transformer(python_list, num_columns))