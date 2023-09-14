#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
datos student
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#%%------------------------------
# Lee datos
data = pd.read_csv('cars.csv',sep=',')
#%%
# Datos para este ajuste

x = data['weight']
y = data['horsepower']

# Ajuste de datos con un polinomio de grado 1
p = np.polyfit(x,y,1)

# Valor para el punto
punto = 3000
valor = np.polyval(p,punto)

# Imprime el valor
print(np.int(valor), 'horse power')

# Valores para dibujar el polinomio
xp = np.linspace(min(x),max(x))
yp = np.polyval(p,xp)

# Plot
plt.figure()
plt.plot(x,y,'o')
plt.plot(xp,yp,'r-')
plt.xlabel('weight')
plt.ylabel('horsepower')
plt.plot(punto, valor, 'ro')
plt.show()

#%%
# Datos para este ajuste
x = data['horsepower']
y = data['mpg']

# Ajuste de datos con un polinomio de grado 2
p = np.polyfit(x,y,2)

# Valor para el punto
punto = valor
valor = np.polyval(p,punto)

# Imprime el valor
print(np.int(valor), ' mpg')

# Valores para dibujar el polinomio
xp = np.linspace(min(x),max(x))
yp = np.polyval(p,xp)

plt.figure()
plt.plot(x,y,'o')
plt.plot(xp,yp,'r-')
plt.xlabel('horsepower')
plt.ylabel('mpg')
plt.plot(punto, valor, 'ro')
plt.show()
#%%