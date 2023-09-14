# -*- coding: utf-8 -*-
"""
Gráfica d la función exponencial con maya gruesa (5 puntos)
"""

import numpy as np
import matplotlib.pyplot as plt

f = lambda x : np.exp(x)
x = np.linspace(-1,1,100)
y = f(x)
plt.plot(x,y)
plt.grid()