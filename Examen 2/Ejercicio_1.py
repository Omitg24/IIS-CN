# -*- coding: utf-8 -*-
"""
Omar Teixeira González, UO281847
Ejercicio 1:
a) Escribir una función nn(x,y,x0) que dados los puntos de interpolación cuyas
coordenadas x e y están almacenadas en los vectores numpy x e y, para un punto x0
calcula y devuelve el valor de interpolación y0, tomando como tal el valor del vecino más 
cercano (en el sentido de distancia entre las coordenadas x) y, a igualdad de distancia, el valor
del vecino más cercano cuyo valor y sea menor.

Los puntos de interpolación serán

    x = np.array([-1., 0, 2, 3, 5, 6, 7])
    y = np.array([1., 3, 4, 3, 2, 2, 1])
    
Y calcularemos los valores de interpolación para los puntos contenidos en el vector
    
    x0 = np,array([-1., 1.3, 2.5, 3, 3.2, 5, 6.5, 7])
    
Representar los puntos de interpolacion y los puntos interpolados.
"""
#%%
import numpy as np
import matplotlib.pyplot as plt

#%%
"""
Búsqueda del indice del vecino
"""
def searchNeighbour(x, y, x0):
    if (len(x)==len(y)):
        index = 0
        minDistancia=np.inf
        for i in range(len(x)):
            distancia = abs(x[i]-x0)
            if (distancia < minDistancia):
                minDistancia=distancia
                index = i
            elif (distancia==minDistancia):
                if (y[i] < y[index]):
                    index = i
                    
        return index
    else:
        print("El tamaño de los vectores de coordenadas no puede ser distinto")

def nn(x, y, x0):
    result = np.zeros(len(x0))
    result[0] = y[0]
    result[-1] = y[-1]
    for i in range(1, len(x0)-1):
        previous = x[i-1]
        following = x[i]
        if (x0[i] == previous):
            result[i]=y[i-1]
        elif (x0[i] == following):
            result[i] = y[i]
        else:
            neighbour = searchNeighbour(x, y, x0[i])
            result[i] = y[neighbour]        
    
    """Dibujar los puntos de interpolación y los interpolados"""
    plt.figure()
    plt.scatter(x, y, linewidths = 9, color = 'green', label = 'Puntos de interpolación')
    plt.scatter(x0, result, linewidths = 1, color = 'red', label = 'Puntos interpolados')    
    plt.legend(loc='best')
    plt.plot()    
    plt.show()

#%%
x = np.array([-1., 0, 2, 3, 5, 6, 7])
y = np.array([1., 3, 4, 3, 2, 2, 1])
x0 = np.array([-1., 1.3, 2.5, 3, 3.2, 5, 6.5, 7])

nn(x, y, x0)
#%%
"""
b) Escribir una función nnv(x, y, xp) que devuelve los valores de interpolación
para los puntos de 

    xp=np,linspace(min(x), max(x))

en un vector yp. Dibujar los nodos y los valores interpolados.
"""

#%%
def lagrange(k,x,z):
    n = len(x)

    ypf = 1.

    for i in range(n):
        if k != i :
            ypf *= (z-x[i]) / (x[k]-x[i]) 
    
    return ypf 

def nnv(x, y, xp):
    n = len(x)
    yp = 0.
    for k in range(n):
        yp += y[k] * lagrange(k,x,xp)
    return yp

#%%
x = np.array([-1., 0, 2, 3, 5])
y = np.array([ 1., 3, 4, 3, 1])


xp = np.linspace(min(x),max(x))
yp = nnv(x,y,xp)

"""Dibujar"""
plt.figure()
plt.plot(x,y,'ro',label='puntos')
plt.plot(xp,yp,label='P')
plt.legend()
plt.show()   