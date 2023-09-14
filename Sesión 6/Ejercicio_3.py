## module cheby
# -*- coding: utf-8 -*-
"""
cheby(f,a,b,n)
"""
import numpy as np
import matplotlib.pyplot as plt


def chebyshev(f,a,b,n):
    # nodos equiespaciados
    xe = np.linspace(a,b,n)
    
    # nodos chebyshev
    index2 = np.arange(1,n+1)
    xc=np.cos(((2.*index2-1)*np.pi)/(2.*n))
    
    # x para los plots
    xx=np.linspace(a,b,500)
    
    # polinomio nodos equiespaciados
    pe=np.polyfit(xe,f(xe),n-1)
    # polinomio nodos chebyshev
    pc=np.polyfit(xc,f(xc),n-1)  
    
    plt.figure()   
    plt.plot(xx,f(xx),'b',label=u'función')
    plt.plot(xe,f(xe),'ro',label='nodos')
    plt.plot(xx,np.polyval(pe,xx),'r',label='polinomio')
    plt.title('Nodos equiespaciados')
    plt.axis([-1.05, 1.05, -0.3, 2.3])
    plt.legend(loc='best')
    plt.show()
    
    plt.figure() 
    plt.plot(xx,f(xx),'b',label=u'función')
    plt.plot(xc,f(xc),'ro',label='nodos')
    plt.plot(xx,np.polyval(pc,xx),'r',label='polinomio')
    plt.title('Nodos Chebyshev')
    plt.axis([-1.05, 1.05, -0.3, 2.3])
    plt.legend(loc='upper center')
    plt.show()
#-------------------------------------------------------
f = lambda x : 1/(1+25*x**2) # definimos la función
a = -1.; b =  1.; n = 11  
print('------------  Función f1  ------------')
chebyshev(f,a,b,n)  
#-------------------------------------------------------
f = lambda x : np.exp(-20*x**2) # definimos la función
a = -1.; b =  1.; n = 15   
print('\n\n------------  Función f2  ------------')
chebyshev(f,a,b,n)   
       
