# -*- coding: utf-8 -*-
"""
Ejercicios
"""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
#%%
def plotting(f,a,b,nodos):
    plt.figure()
    ## Área exacta (función: blue 'b')
    # función (parte de arriba)
    xp = np.linspace(a,b) # 50  points
    plt.plot(xp,f(xp),'b',label = 'Área exacta')
    # Cierre
    plt.plot([a,a,b,b],[f(a),0,0,f(b)],'b')
    
    # Puntos de interpolación (puntos rojos: 'ro')
    plt.plot(nodos,f(nodos),'ro',label = 'Puntos de interpolación')
    
    # Área aproximada (Línea discontinua roja: 'r--')
    # Polinomio interpolante
    p = np.polyfit(nodos,f(nodos),len(nodos)-1)
    xp = np.linspace(a,b) # 50  points
    yp = np.polyval(p,xp)
    plt.plot(xp,yp,'r--',label = 'Área aproximada')
    # Cierre
    pa = np.polyval(p,a)
    pb = np.polyval(p,b)
    plt.plot([a,a,b,b],[pa,0,0,pb],'r--')
    
    plt.legend()
    plt.show()
#%%
def punto_medio(f,a,b,n=1,plot=False):
    # implementa la formula
    xm = (a+b)/2
    Ia = (b-a) * f(xm)
    
    if plot:
        nodos = np.array([xm])
        plotting(f,a,b,nodos)
    
    return Ia
#%%
def trapecio(f,a,b,n=1,plot=False):
    # implementa la formula
    Ia = (b-a) * (f(a)+f(b))/2
    
    if plot:
        nodos = np.array([a,b])
        plotting(f,a,b,nodos)
    
    return Ia
#%%
def simpson(f,a,b,n=1,plot=False):
    # implementa la formula
    xm = (a+b)/2
    Ia = (b-a)/6 * (f(a)+4*f(xm)+f(b))
    
    if plot:
        nodos = np.array([a,xm,b])
        plotting(f,a,b,nodos)
    
    return Ia
#%%
def punto_medio_comp(f,a,b,n):
    x = np.linspace(a,b,n+1)
    Ia = 0.
    for i in range(n):
        Ia += punto_medio(f,x[i],x[i+1])
    return Ia   
#%%
def trapecio_comp(f,a,b,n): 
    x = np.linspace(a,b,n+1)
    Ia = 0.
    for i in range(n):
        Ia += trapecio(f,x[i],x[i+1])
    return Ia  
#%%
def simpson_comp(f,a,b,n): 
    x = np.linspace(a,b,n+1)
    Ia = 0.
    for i in range(n):
        Ia += simpson(f,x[i],x[i+1])
    return Ia 
#%%
def gauss(f,a,b,n,plot=False):
    
    [x, w] = np.polynomial.legendre.leggauss(n)
    y = (b-a)/2 * x + (b+a)/2
    Ia = np.sum(w * f(y)) * (b-a)/2  
    
    if plot:
        plotting(f,a,b,y)
    
    return Ia
#%%
def grado_de_precision(formula,n):
    i = 0
    error = 0.
    x = sym.Symbol('x', real=True)
    while i < 20 and error < 1.e-10:
        Ie = float(sym.integrate(x**i,(x,1,3)))
        f = lambda t: t**i
        Ia = formula(f,1,3,n)
        error = np.abs(Ie-Ia)
        i += 1
        
        print('f(x) = x^'+str(i-1),'   error = ',error)
        
    print('\nEl grado de precisión de la fórmula es ',i-2) 
#%%-----------------------------------------------
x = sym.Symbol('x', real=True) 
f_sym = sym.log(x)
Ie = sym.integrate(f_sym,(x,1,3))
Ie = float(Ie)
#%%
f = lambda x: np.log(x)
a = 1.; b = 3.; n = 1
#%%  Ejercicio 1 ----------------------------------
print('\nEjercicio 1a: punto medio\n')
Ia = punto_medio(f,a,b,n,plot=True)
print('El valor aproximado es  ',Ia)
print('El valor exacto es      ',Ie)
#%%
print('\nEjercicio 1b: trapecios\n')
Ia = trapecio(f,a,b,n,plot=True)
print('El valor aproximado es  ',Ia)
print('El valor exacto es      ',Ie)
#%%
print('\nEjercicio 1c: simpson\n')
Ia = simpson(f,a,b,n,plot=True)
print('El valor aproximado es  ',Ia)
print('El valor exacto es      ',Ie)
#%%
print('\nEjercicio 1d: puntos medio compuesta\n')
n = 5
Ia = punto_medio_comp(f,a,b,n)
print('El valor aproximado es  ',Ia)
print('El valor exacto es      ',Ie)
#%%
print('\nEjercicio 1e: trapecios compuesta\n')
n = 4
Ia = trapecio_comp(f,a,b,n)
print('El valor aproximado es  ',Ia)
print('El valor exacto es      ',Ie)
#%%
print('\nEjercicio 1f: simpson compuesta\n')
n = 4
Ia = simpson_comp(f,a,b,n)
print('El valor aproximado es  ',Ia)
print('El valor exacto es      ',Ie)
#%%  Ejercicio 2 ----------------------------------
print('\nEjercicio 2: gauss con n = 1\n')
n = 1
Ia = gauss(f,a,b,n,plot=True)
print('El valor aproximado es  ',Ia)
print('El valor exacto es      ',Ie)
#%%
print('\nEjercicio 2: gauss con n = 2\n')
n = 2
Ia = gauss(f,a,b,n,plot=True)
print('El valor aproximado es  ',Ia)
print('El valor exacto es      ',Ie)
#%%
print('\nEjercicio 2: gauss con n = 3\n')
n = 3
print('El valor aproximado es  ',Ia)
print('El valor exacto es      ',Ie)
#%%  Ejercicio 3 ----------------------------------
print('\n----  Fórmula del punto medio (1 punto) ----\n')
grado_de_precision(punto_medio,1)
#%%
print('\n----  Fórmula del trapecio (2 puntos) ----\n')
grado_de_precision(trapecio,1)
#%%
print('\n----  Fórmula de Simpson (3 puntos) ----\n')
grado_de_precision(simpson,1)
#%%
print('\n----  gauss n = 1 ----\n')
grado_de_precision(gauss,1)
#%%
print('\n----  gauss n = 2 ----\n')
grado_de_precision(gauss,2)
#%%
print('\n----  gauss n = 3 ----\n')
grado_de_precision(gauss,3)
#%%
print('\n----  gauss n = 4 ----\n')
grado_de_precision(gauss,4)