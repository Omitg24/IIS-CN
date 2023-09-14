# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:14:20 2022

@author: omart
"""

import numpy as np
import matplotlib.pyplot as plt

def busquedaIncremental(f, a, b, n):
    x = np.linspace(a,b,n+1)
    intervalos = np.zeros((n,2))
    contador = 0
    y = f(x)
    
    for i in range(n):
        if y[i]*y[i+1] < 0:
            intervalos[contador,:] = x[i:i+2]
            contador += 1
    
    intervalos = intervalos[:contador:]
    return intervalos

f = lambda x : x**5 - 3 * x**2 + 1.6   # definimos la función
x = np.linspace(-1,1.5)                # definimos un vector con 50 elementos en (-1,1.5)
ox = 0*x                               # definimos un vector de ceros del tamaño de x

print(busquedaIncremental(f,-1,1.5,25));

g = lambda x : (x+2)*np.cos(2*x)
x = np.linspace(0,10)
ox = 0*x
print(busquedaIncremental(g,0,10,100));

plt.figure()
plt.plot(x,f(x))                   # dibujamos la función 
plt.plot(x,ox,'k-')                # dibujamos el eje X
plt.show()                         # hemos acabado este gráfico