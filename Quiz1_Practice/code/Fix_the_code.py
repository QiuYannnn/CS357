# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 12:11:59 2021

@author: Einsgate
"""

def consecutive_elem_ratio(seq):
    temp = []
    for i in range(1, len(seq)):
        ratio = seq[i]/seq[i-1]
        temp.append(ratio)
    
    for i in range(len(seq)):
        seq.pop()
    for i in range(len(temp)):
        seq.append(temp[i])
fibonnaci_seq = [1, 1, 2, 3, 5, 8, 13, 21]
consecutive_elem_ratio(fibonnaci_seq)
print(fibonnaci_seq)
