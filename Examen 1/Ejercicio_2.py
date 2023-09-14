# -*- coding: utf-8 -*-
"""
Omar Teixeira González, UO281847
Ejercicio 2:
Escribir una función derivada(p) que devuelva los coeficientes de un polinomio p.

Tener en cuenta que si 
    P(x) = p0x^n + p1*x^n-1 + ... + pn-2*x^2 + pn-1*x + pn
entonces 
    P'(x) = n*p0*x^n-1 + (n-1)*p1*x^n-2 + ... + 2*pn-2*x + pn-1
    
Es decir, para derivar recortamos un elemento del vector p y multiplicamos los 
elementos del vector resultante respectivamente por
    n, n-1,..., 2, 1

Probar la función con
    p = np.zeros(7)
    T4 = np.array([8., 0, -8, 0, 1])
"""

#%%

import numpy as np

def derivada(p):
    p_Derivado = np.zeros(len(p)-1)
    counter = 0
    for i in range(len(p)-1, 1, -1):
        p_Derivado[counter]=p[counter]*i
        counter += 1
        
    return p_Derivado

#%%        
p = np.zeros(7)
T4 = np.array([8., 0, -8, 0, 1])

#Ejecución de los métodos
print("Derivada de P = ", derivada(p))
print("Derivada de T4 = ", derivada(T4))
