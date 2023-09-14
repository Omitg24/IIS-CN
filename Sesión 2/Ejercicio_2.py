# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 16:00:56 2022

@author: omart
"""
import numpy as np

def P(rango):
    tol = 1.e-8
    maxNumSum = 100
     
    polinomio = 0.
    factorial = 1.
    test_parada = False
    
    iter=0.
    
    for i in range(rango):    
        while (test_parada == False):
            sumando = i**iter/factorial
            polinomio += sumando
            test_parada = max(abs(sumando)) < tol and max(abs(sumando)) < maxNumSum
            iter += 1
            factorial += iter
    
        print("Valor de la función en ", i, "\t= ", polinomio)
        print("Valor de la aproximacion en ", i, "\t= ", polinomio)
        print("Número de iteraciones \t= ", iter)

def Main():
    rango=np.linspace(-1,1)
    P(rango)

