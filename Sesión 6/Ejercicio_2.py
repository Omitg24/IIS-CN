# -*- coding: utf-8 -*-
"""
Ejercicio 3
"""
import numpy as np
import matplotlib.pyplot as plt
#%%----------------------------------------------------------------------------
def lagrange_fundamental(k,x,z):
    n = len(x)

    ypf = 1.

    for i in range(n):
        if k != i :
            ypf *= (z-x[i]) / (x[k]-x[i]) 
    
    return ypf 
#%%----------------------------------------------------------------------------
def polinomio_lagrange(x,y,xp):
    n = len(x)
    yp = 0.
    for k in range(n):
        yp += y[k] * lagrange_fundamental(k,x,xp)
    return yp
#%%----------------------------------------------------------------------------

x = np.array([-1., 0, 2, 3, 5])
y = np.array([ 1., 3, 4, 3, 1])


xp = np.linspace(min(x),max(x),100)
yp = polinomio_lagrange(x,y,xp)

plt.figure()
plt.plot(x,y,'ro',label='puntos')
plt.plot(xp,yp,label='P')
plt.legend()
plt.show()   
#%%----------------------------------------------------------------------------
x = np.array([-1., 0, 2, 3, 5, 6, 7])
y = np.array([ 1., 3, 4, 3, 2, 2, 1])

xp = np.linspace(min(x),max(x),100)
yp = polinomio_lagrange(x,y,xp)

plt.figure()
plt.plot(x,y,'ro',label='puntos')
plt.plot(xp,yp,label='P')
plt.legend()
plt.show() 

    