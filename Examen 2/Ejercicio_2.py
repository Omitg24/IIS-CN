# -*- coding: utf-8 -*-
"""
Omar Teixeira González, UO281847
Ejercicio 2:
Escribir una función det_diag(A) que transforme una matriz cuadrada
en triangular inferior realizando unicamente operaciones por filas tipo

    fi <- fi + λfj i=/=j
    
y devuelva la matriz transformada y su determinante.

Empezar utilizando como ecuación pivotal la última e ir ascendiendo 
hasta la primeroa.

Algoritmo
    Para k = n, ..., 2
        Si akk=0, acabar
        Caso contrario, para i = k-1, ..., 1,
            f = aik/akk
            fila i de a <- fila i de a - f * fila k de a

    Transformar y calcular el determinante de las siguientes matrices
    
A1 = np.array([[2., 1, 1],[1, 2, 1], [1, 1, 2]])

n=5
np.random.seed(3)
A2 = np.random.random((n,n))

n=2
np.random.seed(4)
A2 = np.random.random((n,n))
"""

#%%
import numpy as np

#%%
def det_diag(A):
    if (len(A)==len(A[0])):    
        n=len(A)
        X=np.copy(A)              
        for k in range(n-1,0,-1):
            if (X[k][k]==0):
                break;
            else:
                for i in range(k-1, -1, -1):
                    f=X[i][k]/X[k][k]
                    X[i]=X[i]-f*X[k]                    
        return X, np.linalg.det(X)
    else:
        return "La matriz debe de ser cuadrada";    
#%%
A1 = np.array([[2., 1, 1],
               [1, 2, 1], 
               [1, 1, 2]])

print("Ejemplo 1:")
A, detA = det_diag(A1)
print(A)
print(detA)

n=5
np.random.seed(3)
A2 = np.random.random((n,n))

print("\nEjemplo 2:")
A, detA = det_diag(A2)
print(A)
print(detA)

n=2
np.random.seed(4)
A3 = np.random.random((n,n))

print("\nEjemplo 3:")
A, detA = det_diag(A3)
print(A)
print(detA)