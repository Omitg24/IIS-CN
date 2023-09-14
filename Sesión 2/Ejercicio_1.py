# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 16:00:56 2022

@author: omart
"""


x0 = -0.4
tol = 1.e-8
maxNumSum = 100
 
polinomio = 0.
factorial = 1.
test_parada = False

iter=0.
    
while (test_parada == False and iter < maxNumSum):
    sumando = x0**iter/factorial
    polinomio += sumando
    test_parada = abs(sumando) < tol
    iter += 1
    factorial += iter

print("Valor de la función en ", x0, "\t= ", polinomio)
print("Valor de la aproximacion en ", x0, "\t= ", polinomio)
print("Número de iteraciones \t= ", iter)