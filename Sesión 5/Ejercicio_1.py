# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 15:20:10 2022

@author: omart
"""

import numpy as np
import matplotlib.pyplot as plt

def secante(f, x0, x1, tol = 1.e-6, maxiter=100):
    
    i = 0
    while (i < maxiter):
        if (abs(x1-x0) < tol):
            break;
        else:
            tmp = x0
            x0 = x1
            x1 = x1 - (f(x1)*(x1-tmp)/(f(x1)-f(tmp)))
            i += 1
            
    return x1, i;

f = lambda x: x**5 - 3 * x**2 + 1.6  # definimos la función f
r = np.zeros(3)

tol = 1.e-6; maxiter = 100

x0 = -0.7; x1 = -0.6
r[0], i1 = secante(f,x0,x1,tol,maxiter)
print(r[0],i1)

x0 = 0.8; x1 = 0.9
r[1], i2 = secante(f,x0,x1,tol,maxiter)
print(r[1], i2)

x0 = 1.2; x1 = 1.3
r[2], i3 = secante(f,x0,x1,tol,maxiter)
print(r[2], i3)  

plt.figure()
x = np.linspace(-1,1.5)
plt.plot(x,f(x),x,0*x,'k',r,r*0,'ro')
plt.show()