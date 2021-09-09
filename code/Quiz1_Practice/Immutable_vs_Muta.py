# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 12:05:39 2021

@author: Einsgate
"""


a = 'C'
Ja = (a,'S')
Je = Ja
a = 'F'
Je += ('and','E')
print(Ja, Je)

a = 'C'
Ja = [a,'S']
Je = Ja
a = 'F'
Je += ['and','E']
print(Ja, Je)



a = '012345678'
b = a
b += "910"
print(a)

a = (0,1,2,3,4,5,6,7,8)
b = a.copy()
b += (9,10)
print(a)

a = [0,1,2,3,4,5,6,7,8]
b = a
b += [9,10]
print(a)

