# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 15:15:21 2022

Algoritmo de Horner

@author: omart
"""

import numpy as np
import matplotlib.pyplot as plt 

def hornerV(p, x):
    y = np.zeros_like(x)
    for j in range(len(x)):        
        for i in range(len(p)):
            y[i]=p[i]+y[i-1]*x[j]
        
    cociente = y[:-1]
    resto = y[-1]
    return cociente,resto 

x = np.linspace(-1,1)
p = np.array([1., -1, 2, -3, 5, -2])
r = np.array([1., -1, -1, 1, -1, 0, -1, 1])

plt.figure()
plt.plot(x,np.polyval(p,x))
plt.plot(x,0*x,'k')
plt.title('Polinomio P')
plt.show()

plt.figure()
plt.plot(x,np.polyval(r,x))
plt.plot(x,0*x,'k')
plt.title('Polinomio P')
plt.show()