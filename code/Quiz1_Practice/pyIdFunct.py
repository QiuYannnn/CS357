# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 13:05:53 2021

@author: Einsgate
"""
def foo(x):
    x = x * 4
    return id(x)
q = ['abc', 'def']
print(id(q) == foo(q))