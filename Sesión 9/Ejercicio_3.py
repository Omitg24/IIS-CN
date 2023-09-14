# -*- coding: utf-8 -*-
"""
Ejercicio 3
"""
import numpy as np
np.set_printoptions(precision = 2)  
np.set_printoptions(suppress = True)
#%%
def gaussjordan(A):
    n = len(A)
    I = np.eye(n)
    m = np.concatenate((A,I),axis=1)
    
    for k in range(n):
        m[k] /= m[k,k]
        for i in range(n):
            if i != k:
                m[i] -= m[i,k] * m[k]
    return m[:,n:]   
#%%         
A = np.array([[2., 1, 1], [1, 2, 1], [1, 1, 2]])
print('Matriz')
print(A)
print('Inversa')
print(gaussjordan(A))

#%%
n = 5
np.random.seed(3)           
A = np.random.random((n,n)) 
print('Matriz')
print(A)
print('Inversa')
print(gaussjordan(A))







        
