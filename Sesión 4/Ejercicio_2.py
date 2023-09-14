# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:14:20 2022

@author: omart
"""

def biseccion(f,a,b,tol=1.e-6,maxIter=100):
    if f(a)*f(b) > 0:
        print("f tiene el mismo signo en los extremos")
        return 0;
    for i in range(maxIter):
        m = (a+b)/2
        if (f(a)*f(b)<0):
            b=m
        elif (f(m)*f(b)<0):
            a=m
        else:
            break        
        if (b-a<tol):
            break
    return m, i+1
    
    
f = lambda x : x**5 - 3 * x**2 + 1.6   # definimos la función

a = -0.7; b = -0.6
sol1, i1 = biseccion(f,a,b)
print(sol1, i1)


a = 0.8; b = 0.9
sol2, i2 = biseccion(f,a,b)
print(sol2, i2)

a = 1.2; b = 1.3
sol3, i3 = biseccion(f,a,b)
print(sol3, i3)