# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 15:14:20 2022

@author: omart
"""

def newton(f,df,x0,tol=1.e-6,maxIter=100):    
    for i in range(maxIter):
        x = x0 - f(x0)/df(x0)        
        if (abs(x-x0)<tol):
            break
        x0 = x        
    return x0, i+1
    
f = lambda x : x**5 - 3 * x**2 + 1.6   # definimos la función
df = lambda x : 5*x**4 - 6.*x

x0 = -0.7
sol1, i1 = newton(f,df,x0)
print(sol1, i1)

x0 = 0.8
sol2, i2 = newton(f,df,x0)
print(sol2, i2)

x0 = 1.2
sol3, i3 = newton(f,df,x0)
print(sol3, i3)