# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 15:28:05 2022

@author: omart
"""
import numpy as np
import time

f = lambda x: np.exp(x)
z = np.linspace(-10,10,1000000)   # vector con un millón de elementos
zy = np.zeros_like(z)             # vector de ceros con la misma estructura que z

t = time.time()
for i in range(len(z)):           
    zy[i] = f(z[i])
t1 = time.time()-t      
print('Sin vectorización: ', t1, ' segundos')

t = time.time()
zy = f(z)
t1 = time.time()-t   
print('Con vectorización: ', t1,' segundos') 