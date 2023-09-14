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

def derPol(p, x0):
    n = len(p)
    der = np.zeros_like(p)
    factorial = 1.
    for i in range(n):
        q, resto = horner(p, x0)
        der[i]=resto*factorial
        p=q
        factorial *=i+1
    return der

np.set_printoptions(suppress = True)

p = np.array([1., -1, 2, -3,  5, -2])
x0 = 1.
print("Derivadas sucesivas de P en x0 = ", x0)
print(derPol(p, x0))

r = np.array([1., -1, -1, 1, -1, 0, -1, 1])
x1 = -1.
print("Derivadas sucesivas de R en x1 = ", x1)
print(derPol(r, x1))