# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 16:41:33 2020

@author: Dhanush Wagle
"""

import numpy as np
import matplotlib.pyplot as plt

def y_exact(t):
    return (np.sqrt(2)/(np.sqrt(7*np.exp(2*t) + 2*t +1)))

a = 0; b = 4; n = 100
dt = float(b-a)/n

y_FE = np.zeros(n+1)
y_BE = np.zeros(n+1)
t = np.zeros(n+1)

y_FE[0] = 0.5
y_BE[0] = 0.5

for i in range(0, n, 1):
    dyFdt = t[i]*y_FE[i]**3 - y_FE[i]
    y_FE[i+1] = y_FE[i] + dt*dyFdt
    
    dyBdt = t[i]*y_BE[i]**3 - y_BE[i]
    y_BE[i+1] = y_BE[i] / (1.0 - dt*dyBdt)

t_num = np.linspace(a, b, n+1)
t_true = np.linspace(a, b, 1000)
y_true = y_exact(t_true)

plt.plot(t_true, y_true, '-b', t_num, y_FE, 'r--', t_num, y_BE, 'g--')
plt.legend(['exact', 'FE', 'BE'], loc='upper right')
plt.xlabel('t [sec]')
plt.ylabel('y (t)')
plt.grid()
plt.show()
            