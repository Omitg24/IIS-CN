# -*- coding: utf-8 -*-
"""
Omar Teixeira González, UO281847
Ejercicio 3:
Escribe una función llamada NewtonRaphson que calcule las raíces 
haciendo uso del método de Newton-Raphson con un error absoluto menor que 10.e-6.

Dibuja la función en el intervalo [0,2].
Halla las raíces en dicho intervalo.
"""

#%%

import numpy as np
import matplotlib.pyplot as plt

def NewtonRaphson(f,df,x0,tol=10.e-6,maxIter=100):    
    for i in range(maxIter):
        x = x0 - f(x0)/df(x0)      
        if ((abs(x - x0)) < tol):                   
            break
        x0 = x
        
    return x,i+1

#%%
f = lambda x : np.sin(2*x+3) + np.cos(x)    #Función f
df = lambda x : 2*np.cos(2*x+3) - np.sin(x) #Derivada de la función f

x0 = 0
x1 = 2

#Ejecución de los métodos
raiz0, iterNum0 = NewtonRaphson(f,df,x0)    #Ejecución de NewtonRaphson con entrada 0
print("f tiene una raiz aproximadamente en: ", raiz0, "\n\tCon un total de :", iterNum0, " iteraciones")

raiz1, iterNum1 = NewtonRaphson(f,df,x1)    #Ejecución de NewtonRaphson con entrada 2
print("f tiene una raiz aproximadamente en: ", raiz1, "\n\tCon un total de :", iterNum1, " iteraciones")

#Dibujo de la grafica
x = np.linspace(x0,x1,50)
plt.figure()
plt.plot(x,f(x),"g-",label = 'Función f')
plt.plot([x0,x1],[0,0],'k-')
plt.legend(loc='best')
plt.plot(raiz0,0,'bo',label='punto fijo')
plt.plot(raiz1,0,'bo',label='punto fijo')
plt.show()