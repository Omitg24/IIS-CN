import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi,2*np.pi,200)            
f = lambda x : x*np.sin(3*x)  
OX = 0*x                  

plt.figure()
plt.plot(x,f(x))                  
plt.plot(x,OX,'k-')                
plt.xlabel('x')
plt.ylabel('y')
plt.title('x sen(3x)')
plt.show()