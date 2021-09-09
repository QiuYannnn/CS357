# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 00:03:38 2021

@author: Einsgate
"""

nmax = 5
def func_int(k):
    return k




import math
import numpy as np
If = np.array([])
Ib = np.array([])

I0 = 1-1/math.e
for i in range(nmax):
    If = np.append(If, 0)
    Ib = np.append(Ib, 0)

If[0] = 1 - I0
for i in range(1, nmax):
    If[i] = 1 - (i + 1) * If[i - 1]

Ib[nmax - 1] = 0
for i in range(nmax - 1, 0, -1):
    Ib[i - 1] = (1 - Ib[i]) / (i+1)

print(If)
print(Ib)
abserrf = np.array([])
relerrf = np.array([])
abserrb = np.array([])
relerrb = np.array([])

for i in range(nmax):
    abserrf = np.append(abserrf, abs(func_int(i + 1) - If[i]))
    relerrf = np.append(relerrf, abserrf[i] / func_int(i + 1))
    
    abserrb = np.append(abserrb, abs(func_int(i + 1) - Ib[i]))
    relerrb = np.append(relerrb, abserrb[i] / func_int(i + 1))