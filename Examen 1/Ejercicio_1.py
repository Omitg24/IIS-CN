# -*- coding: utf-8 -*-
"""
Omar Teixeira González, UO281847
Ejercicio 1:
Crear una funcion cambios_signo(p) que cuente los cambios de signo entre los 
coeficientes de un polinomio y devuelva ese número entero positivo como salida.
Si algún coeficiente es cero, no se tiene en cuenta.

Utilizarlos para dar el número máximo de raíces positivas con
    p0 = np.array([32., -32, -14, 17, -3])
    p1 = np.array([32., -32, 0, 17, -3])
    T4 = np.array([8., 0, -8, 0, 1])
    T6 = np.array([32., 0, -48, 0, 18, 0, -1])
"""

#%%

import numpy as np

def cambios_signo(p):
    counter = 0    
    for i in range(0, len(p)-1):
        counterZeros = 1
        while(p[i+counterZeros]==0):
            counterZeros+=1
        if (p[i]*p[i+counterZeros] < 0):
            counter+=1
            
    return counter

#%%
p0 = np.array([32., -32, -14, 17, -3])
p1 = np.array([32., -32, 0, 17, -3])
T4 = np.array([8., 0, -8, 0, 1])
T6 = np.array([32., 0, -48, 0, 18, 0, -1])

#Ejecución de los métodos
print("p0")
print(cambios_signo(p0), " raíces reales positivas como máximo")
print("p1")
print(cambios_signo(p1), " raíces reales positivas como máximo")
print("T4")
print(cambios_signo(T4), " raíces reales positivas como máximo")
print("T6")
print(cambios_signo(T6), " raíces reales positivas como máximo")