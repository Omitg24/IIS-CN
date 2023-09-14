# -*- coding: utf-8 -*-
"""
Gráfica d la función exponencial con maya gruesa (5 puntos)
"""

import numpy as np
import matplotlib.pyplot as plt

f = lambda x : np.exp(x)
x = np.linspace(-1,1)
y = f(x)

plt.figure()
plt.plot(x,y,label='f')
ox=0*x
plt.plot(x,ox, label='Eje OX')
plt.legend()
plt.title('Ejemplo dibujo función f')
plt.grid()
