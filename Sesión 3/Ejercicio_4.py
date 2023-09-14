# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 15:15:21 2022

Algoritmo de Horner

@author: omart
"""

import numpy as np

def divisores(m):
    div = np.zeros(2*m)
    cont=0
    for i in range(1, m+1):
        if np.remainder(m,i)==0:
            div[cont]=i
            div[cont+1]=-i
            cont+=2
    return div[:cont]

print("Divisores de 6 = ", divisores(6));
print("Divisores de 18 = ", divisores(18));
print("Divisores de 20 = ", divisores(20));