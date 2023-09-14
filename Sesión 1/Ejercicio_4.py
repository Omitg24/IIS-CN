import numpy as np
f = lambda x : x*np.exp(x)
print('\nf(2) = ',f(2))
g = lambda z : z/(np.sin(z)*np.cos(z))
print('\ng(pi/4) = ', g(np.pi/4))
h = lambda x,y : x*y/(x**2+y**2)
print('\nh(2,4) = ', h(2,4))	