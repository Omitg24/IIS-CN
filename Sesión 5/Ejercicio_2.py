# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 15:20:10 2022

@author: omart
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op
import sympy as sym

x = sym.Symbol('x', real=True)

f_sim = x**2 + sym.log(2*x+7) * sym.cos(3*x) + 0.1
df_sim = sym.diff(f_sim,x)
d2f_sim = sym.diff(df_sim,x)

f  = sym.lambdify([x], f_sim,'numpy') 
df = sym.lambdify([x], df_sim,'numpy')
d2f = sym.lambdify([x], d2f_sim,'numpy')

a = -1.
b = 3.
x = np.linspace(a,b,1000)

plt.figure()
plt.plot(x,df(x))
plt.plot([a,b],[0,0],'k-')
plt.title('Función derivada de f')
plt.show()

x0 = np.array([-1.,0.,1.,2.,3.])
x1 = op.newton(df,x0,tol=1.e-6,maxiter=100)
mini = x1[d2f(x1) > 0]  
maxi = x1[d2f(x1) < 0]

a = -2.
b = 4.
x = np.linspace(a,b,1000)

plt.figure()
plt.plot(x,f(x),label = 'Función f')
plt.plot([a,b],[0,0],'k-')
plt.plot(mini,f(mini),'go')
plt.plot(maxi,f(maxi),'ro')
plt.show()
print('EXTREMOS')
print(x1)

a = -1.
b = 4.
x = np.linspace(a,b,1000)

plt.figure()
plt.plot(x,d2f(x))
plt.plot([a,b],[0,0],'k-')
plt.title('Función derivada segunda de f')
plt.show()

x0 = np.array([-0.5,0.5,1.5,2.5,3.5])
x1 = op.newton(d2f,x0,tol=1.e-6,maxiter=100)  

a = -1.
b = 4.
x = np.linspace(a,b,1000)

plt.figure()
plt.plot(x,f(x),label = 'Función f')
plt.plot([a,b],[0,0],'k-')
plt.plot(x1,f(x1),'bo',label='Puntos de Inflexión')
plt.legend(loc='best')
plt.show()
print('PUNTOS DE INFLEXIÓN EN [-1,4]')
print(x1)

