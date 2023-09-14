# -*- coding: utf-8 -*-
"""
Exercise 1
"""
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision = 2)   # 2 cifras decimales
np.set_printoptions(suppress = True) # no usar formato exponencial
#%%
def approx1(f,g,a,b,n):
    # Puntos
    x = np.linspace(a,b,n)
    y = f(x)
    
    # Matriz de Vandermonde 
    v = np.ones((n,g+1))
    for i in range(1,g+1):
        v[:,i] = v[:,i-1] * x
    
    # Construye el sistema lineal
    C = np.dot(v.T,v)
    d = np.dot(v.T,y)
    
    # Resuelve el sistema lineal
    p = np.linalg.solve(C,d)
    p = p[::-1]
    
    # Gráficos
    xp = np.linspace(a,b)  # 50 puntos
    yp = np.polyval(p,xp)  # valor del polinomio en estos puntos
    
    plt.figure()
    plt.plot(xp,yp) # polinomio
    plt.plot(x,y,'o') # puntos
    plt.show()
#%%
f = lambda x: np.sin(x)
a = 0.; b = 2.; n = 5; g = 2 
approx1(f,g,a,b,n)  
#%%
f = lambda x: np.cos(np.arctan(x)) - np.log(x+5)
a = -2.; b = 0.; n = 10; g = 4 
approx1(f,g,a,b,n) 
    
    
    
    
    