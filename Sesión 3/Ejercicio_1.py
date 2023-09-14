# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 15:15:21 2022

Algoritmo de Horner

@author: omart
"""

import numpy as np

def horner(p, x0):
    q=np.zeros_like(p)
    for i in range(len(p)):
        q[i]=p[i]+q[i-1]*x0
        
    cociente = q[:-1]
    resto = q[-1]
    return cociente,resto 

p0 = np.array([1.,2,1])
x0 = 1.
c0, r0 = horner(p0, x0)
print("Coeficientes de Q = ", c0)
print("P0(1) = ", r0)

p1 = np.array([1., -1, 2, -3,  5, -2])
x1 = 1.
c1, r1 = horner(p1, x1)
print("Coeficientes de Q = ", c1)
print("P1(1) = ", r1)

p2 = np.array([1., -1, -1, 1, -1, 0, -1, 1])
x2 = -1.
c2, r2 = horner(p2, x2)
print("Coeficientes de Q = ", c2)
print("P2(-1) = ", r2)