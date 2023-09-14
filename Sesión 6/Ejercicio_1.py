# -*- coding: utf-8 -*-
"""
Ejercicio 1
"""
import numpy as np
import matplotlib.pyplot as plt

def lagrange_fundamental(k,x,z):
    n = len(x)

    ypf = 1.

    for i in range(n):
        if k != i :
            ypf *= (z-x[i]) / (x[k]-x[i]) 
    
    return ypf        
#%%----------------------------------------------------------------------------
# MAIN        
x  = np.array([-1., 0, 2, 3, 5])
y = np.array([ 1., 3, 4, 3, 1])

n = len(x)
xp = np.linspace(min(x),max(x),100)

y0 = np.eye(n)

for k in range(n): 
    ypf = lagrange_fundamental(k,x,xp)
    
    plt.figure()
    plt.plot(xp,ypf)
    plt.plot(x,y0[k],'o')
    plt.plot(xp,0*xp,'k-')
    plt.title('L'+str(k),fontsize=18)    
    plt.show()


    